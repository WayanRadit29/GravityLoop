import pygame
from src.visual.sprite_loader import load_sprite


class Meteor:
    def __init__(self, x, y, speed_y=0):
        self.x = x
        self.y = y
        self.speed_y = speed_y  # 0 = idle, >0 = falling

        self.radius = 14
        self.alive = True
        self.exploded = False

        # Load semua sprite sekali
        self.sprite_idle = load_sprite(
            "src/assets/images/meteors/idle.png",
            scale=(40, 40)
        )
        self.sprite_falling = load_sprite(
            "src/assets/images/meteors/falling.png",
            scale=(90, 90)
        )
        self.sprite_explode = load_sprite(
            "src/assets/images/meteors/explode.png",
            scale=(110, 110)
        )

        # Tentukan sprite awal
        if self.speed_y > 0:
            self.sprite = self.sprite_falling
        else:
            self.sprite = self.sprite_idle

    def update(self):
        # Meteor yang sudah meledak tidak bergerak
        if self.exploded:
            return

        if self.speed_y != 0:
            self.y += self.speed_y

    def explode(self):
        """
        Dipanggil saat collision dengan player
        """
        self.exploded = True
        self.speed_y = 0
        self.sprite = self.sprite_explode

    def is_off_screen(self, screen_height):
        # Meteor meledak tidak perlu dihapus langsung
        if self.exploded:
            return False

        return self.y > screen_height + 50

    def render(self, surface):
        if self.sprite:
            rect = self.sprite.get_rect(center=(int(self.x), int(self.y)))
            surface.blit(self.sprite, rect)
        else:
            pygame.draw.circle(
                surface,
                (255, 120, 120),
                (int(self.x), int(self.y)),
                self.radius
            )
