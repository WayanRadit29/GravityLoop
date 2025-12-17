import pygame
from src.visual.sprite_loader import load_sprite


class Meteor:
    def __init__(self, x, y, speed_y=0):
        self.x = x
        self.y = y
        self.speed_y = speed_y  # 0 = idle, >0 = falling

        self.radius = 14
        self.alive = True

        # Tentukan visual state sekali di awal
        if self.speed_y > 0:
            self.sprite = load_sprite(
                "src/assets/images/meteors/falling.png",
                scale=(90, 90)
            )
        else:
            self.sprite = load_sprite(
                "src/assets/images/meteors/idle.png",
                scale=(40, 40)
            )

  
    def update(self):
        if self.speed_y != 0:
            self.y += self.speed_y

    def is_off_screen(self, screen_height):
        return self.y > screen_height + 50

    def render(self, surface):
        if self.sprite:
            rect = self.sprite.get_rect(center=(int(self.x), int(self.y)))
            surface.blit(self.sprite, rect)
        else:
            pygame.draw.circle(surface, (255, 120, 120),
                               (int(self.x), int(self.y)), self.radius)
