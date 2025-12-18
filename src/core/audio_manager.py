import pygame
import os

class AudioManager:
    def __init__(self):
        pygame.mixer.init()
        
        # Click sound
        self.click = pygame.mixer.Sound("src/assets/sounds/sound_effect/sfxgame/pressclick.wav")

        # Lose sound
        self.lose = pygame.mixer.Sound("src/assets/sounds/sound_effect/sfxlose/lose.wav")
        
        # Win sound
        self.finallyrocket = pygame.mixer.Sound("src/assets/sounds/sound_effect/sfxwin/finallyrocket.wav")
        self.win = pygame.mixer.Sound("src/assets/sounds/sound_effect/sfxwin/win.wav")

        # Jump sound
        self.jump = pygame.mixer.Sound("src/assets/sounds/sound_effect/sfxgame/hopjump.wav")
        
        self.has_played_lose = False
        self.has_played_win = False
        
    def play_click(self):
        self.click.play()

    def play_lose(self):
        if not self.has_played_lose:
            self.lose.play()
            self.has_played_lose = True

    def play_win(self):
        if not self.has_played_win:
            self.finallyrocket.play()
            self.win.play()
            self.has_played_win = True

    def play_jump(self):
        self.jump.play()

    def play_lobby_music(self):
        """Memutar musik di menu lobby (mp3)"""
        self.has_played_lose = False
        self.has_played_win = False
        
        path = os.path.join("src", "assets", "sounds", "bgm", "bgminlobby.mp3")
        if os.path.exists(path):
            pygame.mixer.music.load(path)
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1) # looping
        else:
            print(f"Warning: File {path} tidak ditemukan!")

    def play_game_music(self):
        """Memutar musik saat masuk ke gameplay (wav)"""
        path = os.path.join("src", "assets", "sounds", "bgm", "bgmingame.wav")
        if os.path.exists(path):
            pygame.mixer.music.load(path)
            pygame.mixer.music.set_volume(0.4)
            pygame.mixer.music.play(-1)
        else:
            print(f"Warning: File {path} not found!")

    def stop_music(self):
        """Stop all music background"""
        pygame.mixer.music.stop()
        
    def reset_flags(self):
        self.has_played_lose = False
        self.has_played_win = False