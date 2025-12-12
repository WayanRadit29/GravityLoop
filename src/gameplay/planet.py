import pygame
from GravityLoop.src.core.settings import *


class Planet:
    def __init__(self, x, y, radius, gravity_range):
        self.x = x
        self.y = y
        self.radius = radius

        self.gravity_range = gravity_range
        self.gravity_strength = 0.6     # bisa dituning nanti

        self.color = (120, 150, 255)
        self.range_color = (80, 80, 120)

    def render(self, screen):
        # render area gravitasi (sementara sebagai lingkaran transparan)
        pygame.draw.circle(screen, self.range_color, (self.x, self.y), self.gravity_range, 1)

        # render planet
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
