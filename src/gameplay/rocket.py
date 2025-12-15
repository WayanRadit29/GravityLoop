import pygame
import math


class Rocket:
    def __init__(self, x: float, y: float, radius: int = 18):
        self.x = x
        self.y = y
        self.radius = radius

        # Placeholder visual (nanti ganti sprite roket)
        self.color = (220, 220, 220)

    def check_dock(self, player) -> bool:
        """
        Check if player reaches the rocket (win condition).
        """
        dx = self.x - player.x
        dy = self.y - player.y
        distance = math.sqrt(dx * dx + dy * dy)

        return distance < self.radius + player.radius

    def render(self, surface: pygame.Surface):
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
