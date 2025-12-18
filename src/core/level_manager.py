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

    def _easy_level(self):
        planets = [
            Planet(250, 300, 55),
            Planet(400, 200, 50),
            Planet(550, 350, 48),
        ]

        rocket = Rocket(
            self.screen_width - 80,
            self.screen_height // 2
        )

        return {
            "planets": planets,
            "player_spawn_planet_index": 0,
            "blackhole": None,
            "static_meteors": [],
            "meteor_spawner": None,
            "rocket": rocket,
            "name": "EASY"
        }

    def _medium_level(self):
        planets = [
            Planet(200, 420, 48),
            Planet(260, 150, 44),
            Planet(560, 280, 42),
        ]

        static_meteors = [
            Meteor(360, 210),
            Meteor(650, 100),
        ]

        spawner = MeteorSpawner(mode="FROM_STATIC")
        spawner.set_emitters([
            {
                "pos": (360, 210),
                "direction": (0.10, 1),
                "speed": 4.5,
                "interval": 1800
            },
            {
                "pos": (650, 100),
                "direction": (-0.14, 1),
                "speed": 5.2,
                "interval": 2600
            }
        ])

        rocket = Rocket(720, 420)

        return {
            "planets": planets,
            "player_spawn_planet_index": 0,
            "blackhole": None,
            "static_meteors": static_meteors,
            "meteor_spawner": spawner,
            "rocket": rocket,
            "name": "PYRHA"
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
            "meteor_spawner": None,
            "rocket": rocket,
            "name": "HARD"
        }
