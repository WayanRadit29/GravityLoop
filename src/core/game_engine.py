import pygame

from src.core.settings import(
    SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE, FPS, COLOR_BACKGROUND
)

from src.gameplay.player import Player
from src.gameplay.planet import Planet
from src.gameplay.rocket import Rocket
from src.obstacle.meteor import Meteor
from src.obstacle.meteor_spawner import MeteorSpawner
from src.gameplay.collision import check_player_meteor_collision
from src.obstacle.blackhole import BlackHole





class GameEngine:
    def __init__(self):
        self.screen = pygame.display.set_mode(
            (SCREEN_WIDTH, SCREEN_HEIGHT)
        )

        pygame.display.set_caption(WINDOW_TITLE)

        # Clock for FPS control 
        self.clock = pygame.time.Clock()

        # Game state 
        self.running = True

        self.player = Player(
                x=SCREEN_WIDTH // 2,
                y=SCREEN_HEIGHT // 4
                )
        self.planet = Planet(
            SCREEN_WIDTH // 2,
            SCREEN_HEIGHT // 2,
            40
        )

        self.rocket = Rocket(
            SCREEN_WIDTH - 100,
            SCREEN_HEIGHT // 2
        )

        self.static_meteors = [
            Meteor(300, 250),
            Meteor(500, 350),
        ]

        self.meteor_spawner = MeteorSpawner(SCREEN_WIDTH)

        self.blackhole = BlackHole(500, 300, 120)


        self.game_over = False
        self.win = False



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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.release_orbit()



    def update(self):
        if self.game_over or self.win:
            return
        
        if not self.game_over and not self.player.in_blackhole:
            if self.blackhole.check_player_inside(self.player):
                self.blackhole.start_suck(self.player)
        
        if self.player.in_blackhole and not self.player.alive:
            self.game_over = True


        self.planet.apply_gravity(self.player)
        self.player.update()
        current_time = pygame.time.get_ticks()
        self.meteor_spawner.update(current_time, SCREEN_HEIGHT)

        hit_meteor = check_player_meteor_collision(
            self.player,
            self.meteor_spawner.meteors
        )

        if hit_meteor and not self.game_over:
            self.player.crash()
            hit_meteor.explode()
            self.game_over = True


        if self.rocket.check_dock(self.player):
            self.win = True




    def render(self):
        self.screen.fill(COLOR_BACKGROUND)

        # World layer (paling belakang)
        self.blackhole.render(self.screen)
        self.planet.render(self.screen)

        # Obstacles
        self.meteor_spawner.render(self.screen)
        for meteor in self.static_meteors:
            meteor.render(self.screen)

        # Player & goal
        self.player.render(self.screen)
        self.rocket.render(self.screen)

        # UI
        if self.win:
            font = pygame.font.SysFont(None, 42)
            text = font.render("ASTRONAUT RESCUED!", True, (255, 255, 255))
            self.screen.blit(text, (SCREEN_WIDTH // 2 - 160, 40))

        pygame.display.flip()
