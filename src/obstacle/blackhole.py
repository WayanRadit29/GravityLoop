import pygame
import math
from src.visual.sprite_loader import load_sprite


class BlackHole:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

        self.sprite = load_sprite(
            "src/assets/images/blackhole/blackhole.png",
            scale=(radius * 2, radius * 2)
        )

    def check_player_inside(self, player):
        dx = player.x - self.x
        dy = player.y - self.y
        distance = math.sqrt(dx * dx + dy * dy)

        return distance < self.radius

    def start_suck(self, player):
        player.start_blackhole_suck(self)

    def render(self, surface):
        if self.sprite:
            rect = self.sprite.get_rect(center=(int(self.x), int(self.y)))
            surface.blit(self.sprite, rect)
        else:
            pygame.draw.circle(surface, (40, 0, 60),
                               (int(self.x), int(self.y)), self.radius)
