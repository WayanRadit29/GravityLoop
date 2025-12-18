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

    # ================= LEVEL DEFINITIONS =================

    def _easy_level(self):
        planets = [
            Planet(250, 300, 55),   # Planet 1 (starter, paling jauh dari roket)
            Planet(400, 200, 50),   # Planet 2
            Planet(550, 350, 48),   # Planet 3
        ]

        rocket = Rocket(
            self.screen_width - 80,
            self.screen_height // 2
        )

        return {
            "planets": planets,
            "player_spawn_planet_index": 0,  # SPAWN DI PLANET TERJAUH
            "blackhole": None,
            "static_meteors": [],
            "meteor_spawner": None,
            "rocket": rocket,
            "name": "EASY"
        }

    def _medium_level(self):
        planets = [
            Planet(260, 320, 50),
            Planet(420, 220, 45),
            Planet(580, 380, 45),
        ]

        rocket = Rocket(
            self.screen_width - 90,
            self.screen_height // 2
        )

        return {
            "planets": planets,
            "player_spawn_planet_index": 0,
            "blackhole": BlackHole(460, 300, 90),
            "static_meteors": [],
            "meteor_spawner": MeteorSpawner(
                self.screen_width,
                spawn_interval=3000,
                speed_y=4
            ),
            "rocket": rocket,
            "name": "MEDIUM"
        }

    def _hard_level(self):
        planets = [
            Planet(240, 280, 45),
            Planet(380, 180, 42),
            Planet(520, 260, 40),
            Planet(640, 380, 40),
        ]

        rocket = Rocket(
            self.screen_width - 70,
            self.screen_height // 2
        )

        return {
            "planets": planets,
            "player_spawn_planet_index": 0,
            "blackhole": BlackHole(450, 320, 110),
            "static_meteors": [],
            "meteor_spawner": MeteorSpawner(
                self.screen_width,
                spawn_interval=2000,
                speed_y=5
            ),
            "rocket": rocket,
            "name": "HARD"
        }
