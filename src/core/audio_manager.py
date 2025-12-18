import pygame
import os

class AudioManager:
    def __init__(self):
        pygame.mixer.init()
        
        # Click sound
        self.click = pygame.mixer.Sound("src/assets/sounds/sound_effect/sfxgame/pressclick.wav")

        # Lose sounds
        self.lose = pygame.mixer.Sound("src/assets/sounds/sound_effect/sfxlose/lose.wav")
        # Win sounds
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
        # Reset flag agar suara win/lose bisa bunyi lagi di level berikutnya
        self.has_played_lose = False
        self.has_played_win = False
        
        path = os.path.join("src", "assets", "sounds", "bgm", "bgminlobby.mp3")
        if os.path.exists(path):
            pygame.mixer.music.load(path)
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1) # Loop selamanya
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
            print(f"Warning: File {path} tidak ditemukan!")

    def stop_music(self):
        """Berhentikan semua musik background"""
        pygame.mixer.music.stop()