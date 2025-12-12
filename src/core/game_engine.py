import pygame

from src.core.settings import(
    SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE, FPS, COLOR_BACKGROUND
)

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
        # Game logic will go here
        pass

    def render(self):
        self.screen.fill(COLOR_BACKGROUND)
        pygame.display.flip()