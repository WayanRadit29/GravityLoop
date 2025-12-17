import pygame
import os

class PickLevel:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = screen.get_size()
        
        # Path assets
        self.img_path = os.path.join("src", "assets", "images")
        
        # Load Background & Title
        self.bg = pygame.image.load(os.path.join(self.img_path, "lobby", "lobby_bg.png")).convert()
        self.title = pygame.image.load(os.path.join(self.img_path, "picklevel", "pickyourlevel.png")).convert_alpha()
        
        # Load Buttons
        self.btn_easy = pygame.image.load(os.path.join(self.img_path, "picklevel", "easy.png")).convert_alpha()
        self.btn_medium = pygame.image.load(os.path.join(self.img_path, "picklevel", "medium.png")).convert_alpha()
        self.btn_hard = pygame.image.load(os.path.join(self.img_path, "picklevel", "hard.png")).convert_alpha()
        self.btn_home = pygame.image.load(os.path.join(self.img_path, "picklevel", "home.png")).convert_alpha()
        
        self.planet1 = pygame.image.load(os.path.join(self.img_path, "planets", "planet_1.png")).convert_alpha()
        self.planet4 = pygame.image.load(os.path.join(self.img_path, "planets", "planet_4.png")).convert_alpha()
        self.meteor = pygame.image.load(os.path.join(self.img_path, "meteors", "idle.png")).convert_alpha()
        

        # Posisi Tombol
        self.rect_easy = self.btn_easy.get_rect(center=(self.width // 2 - 270, 300))
        self.rect_medium = self.btn_medium.get_rect(center=(self.width // 2 - 5, 300))
        self.rect_hard = self.btn_hard.get_rect(center=(self.width // 2 + 265, 300))
        self.rect_home = self.btn_home.get_rect(center=(self.width // 2, 450))

    def draw(self):
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.planet1, (-300, 200))   # Kiri bawah (Planet Bara)
        self.screen.blit(self.planet4, (500, 72))  # Kanan atas (Planet Hijau)    # Pojok kanan bawah
        self.screen.blit(self.meteor, (100, 60))  
        self.screen.blit(self.title, (self.width // 2 - self.title.get_width() // 2, -50))
        
        
        self.screen.blit(self.btn_easy, self.rect_easy)
        self.screen.blit(self.btn_medium, self.rect_medium)
        self.screen.blit(self.btn_hard, self.rect_hard)
        self.screen.blit(self.btn_home, self.rect_home)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect_easy.collidepoint(event.pos):
                return "LEVEL_1" # Easy
            if self.rect_medium.collidepoint(event.pos):
                return "LEVEL_2" # Medium
            if self.rect_hard.collidepoint(event.pos):
                return "LEVEL_3" # Hard
            if self.rect_home.collidepoint(event.pos):
                return "GO_LOBBY"
        return None