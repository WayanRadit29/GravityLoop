import pygame
import math
from src.core.settings import GRAVITY_CONSTANT
from src.visual.sprite_loader import load_sprite


class Planet:
    def __init__(self, x: float, y: float, radius: int):
        self.x = x
        self.y = y
        self.radius = radius

        # Gravity Tuning (lebih kecil supaya ga overlap antar planet untuk yg Easy)
        self.gravity_radius = radius * 2
        self.gravity_strength = GRAVITY_CONSTANT * 2.2

        # Visual
        self.sprite = load_sprite("src/assets/images/planets/planet_1.png",scale=(self.radius * 2, self.radius * 2))

    def apply_gravity(self, player):
        dx = self.x - player.x
        dy = self.y - player.y
        dist = math.sqrt(dx * dx + dy * dy)

        if dist == 0:
            return

        # Auto orbit kalo masuk radius
        if (
            dist < self.gravity_radius
            and not player.is_orbiting
            and player.release_cooldown == 0
        ):
            player.start_orbit(self)
            return

        # gaya sedot / tarik gravitasi ke planet
        if dist < self.gravity_radius and not player.is_orbiting:
            nx = dx / dist
            ny = dy / dist
            force = self.gravity_strength / dist
            player.apply_force(nx * force, ny * force)

    def render(self, surface: pygame.Surface):
        if self.sprite:
            rect = self.sprite.get_rect(center=(int(self.x), int(self.y)))
            surface.blit(self.sprite, rect)
        else:
            pygame.draw.circle(
                surface,
                (120, 150, 255),
                (int(self.x), int(self.y)),
                self.radius
            )
