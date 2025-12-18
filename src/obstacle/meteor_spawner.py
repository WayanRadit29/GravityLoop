from src.obstacle.meteor import Meteor


class MeteorSpawner:
    def __init__(self, mode="RANDOM", screen_width=None):
        self.mode = mode
        self.screen_width = screen_width

        self.meteors = []

        self.emitters = []
        self.last_spawn_times = []

        self.spawn_interval = 3000
        self.speed_y = 4
        self.last_spawn_time = 0

    # CONFIGURATION METHODS

    def set_random_config(self, spawn_interval=3000, speed_y=4):
        self.spawn_interval = spawn_interval
        self.speed_y = speed_y

    def set_emitters(self, emitters):
        self.emitters = emitters
        self.last_spawn_times = [0 for _ in emitters]

    # UPDATE METHOD

    def update(self, current_time, screen_height):
        if self.mode == "RANDOM":
            self._update_random(current_time)

        elif self.mode == "FROM_STATIC":
            self._update_from_static(current_time)

        for meteor in self.meteors:
            meteor.update()

        self.meteors = [
            m for m in self.meteors
            if not m.is_off_screen(screen_height)
        ]

    # SPAWN UPDATE METHODS

    def _update_random(self, current_time):
        if current_time - self.last_spawn_time >= self.spawn_interval:
            self.spawn_random()
            self.last_spawn_time = current_time

    def _update_from_static(self, current_time):
        for i, emitter in enumerate(self.emitters):
            interval = emitter["interval"]
            last_time = self.last_spawn_times[i]

            if current_time - last_time >= interval:
                self.spawn_from_emitter(emitter)
                self.last_spawn_times[i] = current_time

    # SPAWN METHODS

    def spawn_random(self):
        x = self.screen_width // 2
        y = -50
        meteor = Meteor(x, y, speed_y=self.speed_y)
        self.meteors.append(meteor)

    def spawn_from_emitter(self, emitter):
        x, y = emitter["pos"]
        vx, vy = emitter["direction"]
        speed = emitter["speed"]

        meteor = Meteor(
            x,
            y,
            vx=vx * speed,
            vy=vy * speed
        )
        self.meteors.append(meteor)

    # RENDER METHOD

    def render(self, surface):
        for meteor in self.meteors:
            meteor.render(surface)
