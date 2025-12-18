import pygame
import os
import sys

class Lobby:
    def __init__(self, screen):
        
        self.screen = screen
        self.width, self.height = screen.get_size()
        
        # Path dasar ke folder images
        self.img_path = os.path.join("src", "assets", "images")
        
        # load assets
        self.bg = pygame.image.load(os.path.join(self.img_path, "lobby", "lobby_bg.png")).convert()
        self.logo = pygame.image.load(os.path.join(self.img_path, "lobby", "logo.png")).convert_alpha()
        self.btn_start_img = pygame.image.load(os.path.join(self.img_path, "lobby", "start.png")).convert_alpha()
        self.astronaut = pygame.image.load(os.path.join(self.img_path, "astronot", "idle.png")).convert_alpha()
        
        # load planet ufo meteor
        self.planet1 = pygame.image.load(os.path.join(self.img_path, "planets", "planet_1.png")).convert_alpha()
        self.planet2 = pygame.image.load(os.path.join(self.img_path, "planets", "planet_2.png")).convert_alpha()
        self.ufo = pygame.image.load(os.path.join(self.img_path, "ufo", "idle.png")).convert_alpha()
        self.meteor = pygame.image.load(os.path.join(self.img_path, "meteors", "idle.png")).convert_alpha()

        # setting rect untuk layoutting
        self.btn_start_rect = self.btn_start_img.get_rect(center=(self.width // 2, 480))
        self.logo_rect = self.logo.get_rect(center=(self.width // 2, 150))
        self.astro_rect = self.astronaut.get_rect(center=(self.width // 2, 320))

    def draw(self):
        # bg full screen
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.logo, self.logo_rect)
        
        # gambar hiasan di lobby
        self.screen.blit(self.planet1, (-300, 200))
        self.screen.blit(self.planet2, (300, 10))
        self.screen.blit(self.ufo, (600, 450))
        self.screen.blit(self.meteor, (600, 80))
        
        # gambar logo, astronot, tombol start
        self.screen.blit(self.logo, self.logo_rect)
        self.screen.blit(self.astronaut, self.astro_rect)
        self.screen.blit(self.btn_start_img, self.btn_start_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.btn_start_rect.collidepoint(event.pos):
                print("Tombol Start Diklik! Berpindah ke Game Engine...")
                return "START"
        return None