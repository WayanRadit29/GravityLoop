import pygame
from src.visual.sprite_loader import load_sprite


class Meteor:
    def __init__(self, x, y, vx=0.0, vy=0.0):
        self.x = x
        self.y = y

        self.vx = vx
        self.vy = vy

        self.radius = 14
        self.alive = True
        self.exploded = False

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

        if self.vx != 0 or self.vy != 0:
            self.sprite = self.sprite_falling
        else:
            self.sprite = self.sprite_idle

    def update(self):
        if self.exploded:
            return

        self.x += self.vx
        self.y += self.vy

    def explode(self):
        self.exploded = True
        self.vx = 0
        self.vy = 0
        self.sprite = self.sprite_explode

    def is_off_screen(self, screen_height):
        if self.exploded:
            return False

        return (
            self.y > screen_height + 100
            or self.x < -100
            or self.x > 900
        )

    def render(self, surface):
        rect = self.sprite.get_rect(center=(int(self.x), int(self.y)))
        surface.blit(self.sprite, rect)
