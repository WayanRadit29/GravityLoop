import random
from src.obstacle.meteor import Meteor


class MeteorSpawner:
    def __init__(self, screen_width, spawn_interval=3000, speed_y=4):
        self.screen_width = screen_width
        self.spawn_interval = spawn_interval
        self.speed_y = speed_y

        self.last_spawn_time = 0
        self.meteors = []

    def update(self, current_time, screen_height):
        if current_time - self.last_spawn_time >= self.spawn_interval:
            self.spawn_meteor()
            self.last_spawn_time = current_time

        for meteor in self.meteors:
            meteor.update()

        self.meteors = [
            m for m in self.meteors
            if not m.is_off_screen(screen_height)
        ]

    def spawn_meteor(self):
        x = random.randint(40, self.screen_width - 40)
        y = -50

        speed = random.randint(
            self.speed_y - 1,
            self.speed_y + 1
        )

        meteor = Meteor(x, y, speed_y=speed)
        self.meteors.append(meteor)

    def render(self, surface):
        for meteor in self.meteors:
            meteor.render(surface)
