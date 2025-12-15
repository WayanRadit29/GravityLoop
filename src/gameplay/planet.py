import pygame
import math

from src.core.settings import GRAVITY_CONSTANT

class Planet: 
    def __init__(self, x: float, y: float, radius: int):
        # Posisi
        self.x = x
        self.y = y

        # Physical size
        self.radius = radius

        # Gravity properties
        self.gravity_radius = radius * 3
        self.gravity_strength = GRAVITY_CONSTANT

        # Visual
        self.color = (120, 150, 255)
        self.gravity_color = (80, 80, 120)

    def apply_gravity(self, player):
        # Vector from player to planet
        dx = self.x - player.x
        dy = self.y - player.y

        distance = math.sqrt(dx * dx + dy * dy)

        # Hindari pembagian nol
        if distance == 0:
            return
        
        # Cek apakah player masuk area gravitasu
        if distance < self.gravity_radius:
            # Normalized direction
            nx = dx / distance
            ny = dy / distance

            # Strength falloff (semakin dekat, semakin kuat)

            force = self.gravity_strength / distance

            # Apply force to player
            player.apply_force(
                nx * force, 
                ny * force
            )

    def render(self, surface: pygame.Surface):
            # Draw gravity area (debug / visual cue)
            pygame.draw.circle(
                surface,
                self.gravity_color,
                (int(self.x), int(self.y)),
                int(self.gravity_radius),
                1
            )

            # Draw planet body
            pygame.draw.circle(
                surface,
                self.color,
                (int(self.x), int(self.y)),
                self.radius
            )


