import pygame
import math

from src.visual.sprite_loader import load_sprite



class Player:
    def __init__(self, x: float, y: float):
        # Position
        self.x = x
        self.y = y

        # Velocity
        self.vx = 1.5
        self.vy = 0.0

        # Acceleration
        self.ax = 0.0
        self.ay = 0.0

        # Orbit state
        self.is_orbiting = False
        self.orbit_center = None
        self.orbit_radius = 0.0
        self.orbit_angle = 0.0
        self.orbit_speed = 0.03
        
        # State Release
        self.release_cooldown = 0 


        # Visual
        self.radius = 10
        self.color = (200, 230, 255)
        self.sprite = load_sprite(
            "src/assets/images/astronot/idle.png",
        scale=(32, 32)
        )

    def apply_force(self, fx: float, fy: float):
        self.ax += fx
        self.ay += fy

    def start_orbit(self, planet):
        self.is_orbiting = True
        self.orbit_center = planet

        dx = self.x - planet.x
        dy = self.y - planet.y

        self.orbit_radius = math.sqrt(dx * dx + dy * dy)
        self.orbit_angle = math.atan2(dy, dx)

        self.vx = 0.0
        self.vy = 0.0
    
    def release_orbit(self):

        if not self.is_orbiting:
            return

        release_speed = 6.0
        self.vx = -math.sin(self.orbit_angle) * release_speed
        self.vy =  math.cos(self.orbit_angle) * release_speed

        self.is_orbiting = False
        self.orbit_center = None
        self.release_cooldown = 20




    def update(self):
        if self.release_cooldown > 0:
            self.release_cooldown -= 1

        if self.is_orbiting:
            self.orbit_angle += self.orbit_speed
            self.x = self.orbit_center.x + math.cos(self.orbit_angle) * self.orbit_radius
            self.y = self.orbit_center.y + math.sin(self.orbit_angle) * self.orbit_radius
            return

        # Physics update
        self.vx += self.ax
        self.vy += self.ay

        self.x += self.vx
        self.y += self.vy

        self.ax = 0.0
        self.ay = 0.0


    def render(self, surface: pygame.Surface):
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
