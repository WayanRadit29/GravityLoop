import pygame

from src.core.settings import(
    SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE, FPS, COLOR_BACKGROUND
)

from src.gameplay.player import Player
from src.gameplay.planet import Planet
from src.gameplay.rocket import Rocket




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

    def update(self):
        self.planet.apply_gravity(self.player)
        self.player.update()

        if self.rocket.check_dock(self.player):
            self.win = True




    def render(self):
        self.screen.fill(COLOR_BACKGROUND)

        self.planet.render(self.screen)
        self.player.render(self.screen)
        self.rocket.render(self.screen)

        if self.win:
            font = pygame.font.SysFont(None, 42)
            text = font.render("ASTRONAUT RESCUED!", True, (255, 255, 255))
            self.screen.blit(text, (SCREEN_WIDTH // 2 - 160, 40))




        pygame.display.flip()