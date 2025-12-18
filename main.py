import pygame
from src.core.game_engine import GameEngine

def main():
    pygame.init()

    game = GameEngine()
    game.run()

if __name__ == "__main__":
    main()
