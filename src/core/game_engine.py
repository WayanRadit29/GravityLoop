import pygame

from src.core.settings import (
    SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE, FPS, COLOR_BACKGROUND
)

from src.gameplay.player import Player
from src.gameplay.planet import Planet
from src.gameplay.rocket import Rocket
from src.obstacle.meteor import Meteor
from src.obstacle.meteor_spawner import MeteorSpawner
from src.gameplay.collision import check_player_meteor_collision
from src.obstacle.blackhole import BlackHole
from src.core.audio_manager import AudioManager
from src.core.level_manager import LevelManager
from src.ui.lobby import Lobby


class GameEngine:
    def __init__(self):
        self.screen = pygame.display.set_mode(
            (SCREEN_WIDTH, SCREEN_HEIGHT)
        )
        pygame.display.set_caption(WINDOW_TITLE)

        self.state = "LOBBY"
        self.lobby = Lobby(self.screen)

        self.clock = pygame.time.Clock()
        self.running = True

        # Core systems
        self.audio = AudioManager()
        self.level_manager = LevelManager(SCREEN_WIDTH, SCREEN_HEIGHT)

        # Player (akan di-reset tiap level)
        self.player = Player(
            x=SCREEN_WIDTH // 2,
            y=SCREEN_HEIGHT // 4
        )



        # World objects (default None, diisi oleh level)
        self.planet = None
        self.blackhole = None
        self.rocket = None
        self.meteor_spawner = None
        self.static_meteors = None

        # Game state
        self.game_over = False
        self.win = False

        # Level state
        self.current_level = 1
        self.load_level(self.current_level)

    # ================= LEVEL LOADING =================

    def load_level(self, level_id):
        level_data = self.level_manager.load_level(level_id)

        self.planet = level_data.get("planet")
        self.blackhole = level_data.get("blackhole")
        self.rocket = level_data.get("rocket")
        self.meteor_spawner = level_data.get("meteor_spawner")
        self.static_meteors = level_data.get("static_meteors", [])

        # Reset player state
        self.player.reset(
            x=SCREEN_WIDTH // 2,
            y=SCREEN_HEIGHT // 4
        )

        self.game_over = False
        self.win = False

    # ================= MAIN LOOP =================

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.handle_events()
            self.update()
            self.render()

    # ================= EVENTS =================

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.release_orbit()

                if self.win and event.key == pygame.K_RETURN:
                    self.current_level += 1
                    if self.current_level <= 3:
                        self.load_level(self.current_level)
                    else:
                        self.running = False
            if self.state == "LOBBY":
                action = self.lobby.handle_event(event)
                if action == "START":
                    self.state = "LEVEL_SELECT"


    # ================= UPDATE =================

    def update(self):
        if self.game_over or self.win:
            return

        # ---------- Black Hole Logic (OPTIONAL) ----------
        if (
            self.blackhole is not None
            and not self.player.in_blackhole
        ):
            if self.blackhole.check_player_inside(self.player):
                self.blackhole.start_suck(self.player)

        if self.blackhole is not None:
            if self.player.in_blackhole and not self.player.alive:
                self.game_over = True
                self.audio.play_lose()
                return

        # ---------- Planet Gravity ----------
        if self.planet is not None:
            self.planet.apply_gravity(self.player)

        # ---------- Player ----------
        self.player.update()

        # ---------- Meteor Spawner (OPTIONAL) ----------
        if self.meteor_spawner is not None:
            current_time = pygame.time.get_ticks()
            self.meteor_spawner.update(current_time, SCREEN_HEIGHT)

            hit_meteor = check_player_meteor_collision(
                self.player,
                self.meteor_spawner.meteors
            )

            if hit_meteor:
                self.player.crash()
                hit_meteor.explode()
                self.game_over = True
                self.audio.play_lose()
                return

        # ---------- Static Meteors (OPTIONAL) ----------
        if self.static_meteors:
            hit_static = check_player_meteor_collision(
                self.player,
                self.static_meteors
            )
            if hit_static:
                self.player.crash()
                hit_static.explode()
                self.game_over = True
                self.audio.play_lose()
                return

        # ---------- Out of Screen ----------
        if (
            self.player.x < -50 or
            self.player.x > SCREEN_WIDTH + 50 or
            self.player.y < -50 or
            self.player.y > SCREEN_HEIGHT + 50
        ):
            self.game_over = True
            self.audio.play_lose()
            return

        # ---------- Win ----------
        if self.rocket is not None:
            if self.rocket.check_dock(self.player):
                self.win = True
                self.audio.play_win()

    # ================= RENDER =================

    def render(self):
        self.screen.fill(COLOR_BACKGROUND)

        if self.state == "LOBBY":
            self.lobby.draw()
            pygame.display.flip()
            return

        # World (back layer)
        if self.blackhole is not None:
            self.blackhole.render(self.screen)

        if self.planet is not None:
            self.planet.render(self.screen)

        # Obstacles
        if self.meteor_spawner is not None:
            self.meteor_spawner.render(self.screen)

        if self.static_meteors:
            for meteor in self.static_meteors:
                meteor.render(self.screen)

        # Player & goal
        self.player.render(self.screen)

        if self.rocket is not None:
            self.rocket.render(self.screen)


        # UI
        font = pygame.font.SysFont(None, 24)
        level_text = font.render(
            f"LEVEL {self.current_level}",
            True,
            (255, 255, 255)
        )
        self.screen.blit(level_text, (10, 10))

        if self.win:
            font_big = pygame.font.SysFont(None, 42)
            text = font_big.render(
                "ASTRONAUT RESCUED!",
                True,
                (255, 255, 255)
            )
            self.screen.blit(
                text,
                (SCREEN_WIDTH // 2 - 160, 40)
            )

        pygame.display.flip()
