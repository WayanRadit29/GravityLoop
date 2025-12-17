from src.gameplay.planet import Planet
from src.obstacle.blackhole import BlackHole
from src.obstacle.meteor import Meteor
from src.obstacle.meteor_spawner import MeteorSpawner
from src.gameplay.rocket import Rocket


class LevelManager:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.levels = {
            1: self._easy_level,
            2: self._medium_level,
            3: self._hard_level,
        }

    def load_level(self, level_id):
        if level_id not in self.levels:
            raise ValueError("Level not found")

        return self.levels[level_id]()

    # ===== LEVEL DEFINITIONS =====

    def _easy_level(self):
        return {
            "planet": Planet(self.screen_width // 2, self.screen_height // 2, 50),

            "blackhole": None,

            "static_meteors": [
                Meteor(300, 250),
            ],

            "meteor_spawner": MeteorSpawner(
                self.screen_width,
                spawn_interval=4000,
                speed_y=3
            ),

            "rocket": Rocket(
                self.screen_width - 120,
                self.screen_height // 2
            ),

            "name": "EASY"
        }

    def _medium_level(self):
        return {
            "planet": Planet(self.screen_width // 2, self.screen_height // 2, 45),

            "blackhole": BlackHole(500, 300, 100),

            "static_meteors": [
                Meteor(300, 250),
                Meteor(450, 200),
            ],

            "meteor_spawner": MeteorSpawner(
                self.screen_width,
                spawn_interval=3000,
                speed_y=4
            ),

            "rocket": Rocket(
                self.screen_width - 100,
                self.screen_height // 2
            ),

            "name": "MEDIUM"
        }

    def _hard_level(self):
        return {
            "planet": Planet(self.screen_width // 2, self.screen_height // 2, 40),

            "blackhole": BlackHole(420, 320, 120),

            "static_meteors": [
                Meteor(280, 220),
                Meteor(500, 260),
                Meteor(350, 400),
            ],

            "meteor_spawner": MeteorSpawner(
                self.screen_width,
                spawn_interval=2000,
                speed_y=5
            ),

            "rocket": Rocket(
                self.screen_width - 80,
                self.screen_height // 2
            ),

            "name": "HARD"
        }
