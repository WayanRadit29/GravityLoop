import pygame


class AudioManager:
    def __init__(self):
        pygame.mixer.init()

        # Lose sounds
        self.lose = pygame.mixer.Sound(
            "src/assets/sounds/sound_effect/sfxlose/lose.wav"
        )

        # Win sounds
        self.finallyrocket = pygame.mixer.Sound(
            "src/assets/sounds/sound_effect/sfxwin/finallyrocket.wav"
        )
        self.win = pygame.mixer.Sound(
            "src/assets/sounds/sound_effect/sfxwin/win.wav"
        )

        self.has_played_lose = False
        self.has_played_win = False

    def play_lose(self):
        if not self.has_played_lose:
            self.lose.play()
            self.has_played_lose = True

    def play_win(self):
        if not self.has_played_win:
            self.finallyrocket.play()
            self.win.play()
            self.has_played_win = True
