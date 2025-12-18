import pygame

from src.core.settings import (
    SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE, FPS, COLOR_BACKGROUND
)

from src.gameplay.player import Player
from src.gameplay.collision import check_player_meteor_collision
from src.core.audio_manager import AudioManager
from src.core.level_manager import LevelManager
from src.ui.lobby import Lobby
from src.ui.picklevel import PickLevel
from src.ui.game_over import GameOverOverlay


class GameEngine:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(WINDOW_TITLE)

        self.state = "LOBBY"

        self.lobby = Lobby(self.screen)
        self.pick_level = PickLevel(self.screen)
        self.game_over_ui = GameOverOverlay(self.screen)

        self.clock = pygame.time.Clock()
        self.running = True

        self.audio = AudioManager()
        self.level_manager = LevelManager(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.player = Player(
            x=SCREEN_WIDTH // 2,
            y=SCREEN_HEIGHT // 4
        )

        self.planets = []
        self.blackhole = None
        self.rocket = None
        self.meteor_spawner = None
        self.static_meteors = []

        self.game_over = False
        self.win = False
        self.current_level = 1

        # --- TAMBAHAN: Jalankan musik lobby saat aplikasi dibuka ---
        self.audio.play_lobby_music()

    # ================= LEVEL LOADING =================

    def load_level(self, level_id):
        level_data = self.level_manager.load_level(level_id)

        self.planets = level_data.get("planets", [])
        self.blackhole = level_data.get("blackhole")
        self.rocket = level_data.get("rocket")
        self.meteor_spawner = level_data.get("meteor_spawner")
        self.static_meteors = level_data.get("static_meteors", [])

        spawn_index = level_data.get("player_spawn_planet_index", 0)
        spawn_planet = self.planets[spawn_index]

        self.player.reset(
            x=spawn_planet.x,
            y=spawn_planet.y - spawn_planet.radius - 8
        )

        if self.meteor_spawner:
            self.meteor_spawner.meteors.clear()
            self.meteor_spawner.last_spawn_time = 0

        self.game_over = False
        self.win = False
        
        # --- TAMBAHAN: Ganti musik ke musik gameplay saat level di-load ---
        self.audio.play_game_music()

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.handle_events()
            self.update()
            self.render()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if self.state == "LOBBY":
                action = self.lobby.handle_event(event)
                if action == "START":
                    self.state = "LEVEL_SELECT"

            elif self.state == "LEVEL_SELECT":
                action = self.pick_level.handle_event(event)
                if action == "LEVEL_1":
                    self.start_game(1)
                elif action == "LEVEL_2":
                    self.start_game(2)
                elif action == "LEVEL_3":
                    self.start_game(3)
                elif action == "GO_LOBBY":
                    self.state = "LOBBY"
                    # --- TAMBAHAN: Balik ke musik lobby ---
                    self.audio.play_lobby_music()

            elif self.state == "PLAYING":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.release_orbit()
                    if self.win and event.key == pygame.K_RETURN:
                        self.next_level()

                if self.game_over or self.win:
                    action = self.game_over_ui.handle_event(event)
                    if action == "PICK_LEVEL":
                        self.state = "LEVEL_SELECT"
                        # --- TAMBAHAN: Balik ke musik lobby ---
                        self.audio.play_lobby_music()
                    elif action == "RESTART":
                        self.load_level(self.current_level)
                    elif action == "NEXT" and self.win:
                        self.next_level()
    def update(self):
        if self.state != "PLAYING":
            return

        if self.game_over or self.win:
            return

        if self.blackhole and not self.player.in_blackhole:
            if self.blackhole.check_player_inside(self.player):
                self.blackhole.start_suck(self.player)

        if self.blackhole and self.player.in_blackhole and not self.player.alive:
            self.game_over = True
            self.audio.play_lose()
            return

        for planet in self.planets:
            planet.apply_gravity(self.player)

        self.player.update()

        if self.meteor_spawner:
            current_time = pygame.time.get_ticks()
            self.meteor_spawner.update(current_time, SCREEN_HEIGHT)

            hit = check_player_meteor_collision(
                self.player,
                self.meteor_spawner.meteors
            )
            if hit:
                self.player.crash()
                hit.explode()
                self.game_over = True
                self.audio.play_lose()
                return

        if self.static_meteors:
            hit = check_player_meteor_collision(
                self.player,
                self.static_meteors
            )
            if hit:
                self.player.crash()
                hit.explode()
                self.game_over = True
                self.audio.play_lose()
                return

        if (
            self.player.x < -50 or
            self.player.x > SCREEN_WIDTH + 50 or
            self.player.y < -50 or
            self.player.y > SCREEN_HEIGHT + 50
        ):
            self.game_over = True
            self.audio.play_lose()
            return

        if self.rocket and self.rocket.check_dock(self.player):
            self.win = True
            self.audio.play_win()

    # ================= RENDER =================
    def render(self):
        self.screen.fill(COLOR_BACKGROUND)

        if self.state == "LOBBY":
            self.lobby.draw()
            pygame.display.flip()
            return

        if self.state == "LEVEL_SELECT":
            self.pick_level.draw()
            pygame.display.flip()
            return

        if self.blackhole:
            self.blackhole.render(self.screen)

        for planet in self.planets:
            planet.render(self.screen)

        if self.meteor_spawner:
            self.meteor_spawner.render(self.screen)

        for meteor in self.static_meteors:
            meteor.render(self.screen)

        self.player.render(self.screen)

        if self.rocket:
            self.rocket.render(self.screen)

        if self.game_over:
            self.game_over_ui.draw("MISSION FAILED", (255, 0, 0))
        elif self.win:
            self.game_over_ui.draw("ASTRONAUT RESCUED!", (0, 255, 0))

        pygame.display.flip()

    def start_game(self, level_id):
        self.current_level = level_id
        self.load_level(level_id)
        self.state = "PLAYING"

    def next_level(self):
        self.current_level += 1
        if self.current_level <= 3:
            self.load_level(self.current_level)
        else:
            self.state = "LOBBY"
            # --- TAMBAHAN: Balik ke musik lobby jika tamat ---
            self.audio.play_lobby_music()
