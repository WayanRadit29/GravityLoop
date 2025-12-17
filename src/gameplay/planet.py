import pygame
import math
from src.core.settings import GRAVITY_CONSTANT
from src.visual.sprite_loader import load_sprite



class Planet:
    def __init__(self, x: float, y: float, radius: int):
        self.x = x
        self.y = y
        self.radius = radius

        self.gravity_radius = radius * 4.6
        self.gravity_strength = GRAVITY_CONSTANT * 3

        self.color = (120, 150, 255)
        self.gravity_color = (80, 80, 120)

        #Visual 
        self.sprite = load_sprite(
            "src/assets/images/planets/planet_1.png",
            scale=(self.radius * 2, self.radius * 2)
        )


    def apply_gravity(self, player):
        dx = self.x - player.x
        dy = self.y - player.y
        dist = math.sqrt(dx * dx + dy * dy)

        if dist == 0:
            return

        # Masuk orbit otomatis
        if (
            dist < self.gravity_radius
            and not player.is_orbiting
            and player.release_cooldown == 0 
            ):
                player.start_orbit(self)
                return


        if dist < self.gravity_radius and not player.is_orbiting:
            nx = dx / dist
            ny = dy / dist
            force = self.gravity_strength / dist
            player.apply_force(nx * force, ny * force)

    def render(self, surface: pygame.Surface):
        pygame.draw.circle(
            surface,
            self.gravity_color,
            (int(self.x), int(self.y)),
            int(self.gravity_radius),
            1
        )

        if self.sprite:
             rect = self.sprite.get_rect(center=(int(self.x), int(self.y)))
             surface.blit(self.sprite, rect)
        else:
            pygame.draw.circle(
                surface,
                self.color,
                (int(self.x), int(self.y)),
                self.radius
            )
