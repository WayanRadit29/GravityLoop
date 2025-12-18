import pygame
import math
from src.visual.sprite_loader import load_sprite


class Rocket:
    def __init__(self, x: float, y: float, radius: int = 18):
        self.x = x
        self.y = y
        self.radius = radius

        # Placeholder visual (sprite roket)
        self.color = (220, 220, 220)
        self.sprite = load_sprite("src/assets/images/rocket/rocket.png",scale=(70, 80))


    def check_dock(self, player) -> bool:
        """
        Check if player reaches the rocket (win condition).
        """
        dx = self.x - player.x
        dy = self.y - player.y
        distance = math.sqrt(dx * dx + dy * dy)

        return distance < self.radius + player.radius

    def render(self, surface: pygame.Surface):


        if self.sprite:
            rect = self.sprite.get_rect(center=(int(self.x), int(self.y)))
            surface.blit(self.sprite, rect)
        else:
            # Placeholder rocket body
            pygame.draw.rect(
                surface,
                self.color,
                pygame.Rect(
                    int(self.x - self.radius // 2),
                    int(self.y - self.radius),
                    self.radius,
                    self.radius * 2
                ),
                border_radius=4
            )

            # Nose cone (segitiga)
            pygame.draw.polygon(
                surface,
                self.color,
                [
                    (int(self.x), int(self.y - self.radius - 8)),
                    (int(self.x - self.radius // 2), int(self.y - self.radius)),
                    (int(self.x + self.radius // 2), int(self.y - self.radius)),
                ],
            )
