import pygame
import os

class GameOverOverlay:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = screen.get_size()
        
        self.img_path = os.path.join("src", "assets", "images", "gameover")
        
        # LOAD ASSETS DAN SCALING SUPAYA GA GEDE, JADI 80 X 80
        btn_size = (80, 80) 

        img_levels = pygame.image.load(os.path.join(self.img_path, "backtolevels.png")).convert_alpha()
        self.btn_levels = pygame.transform.smoothscale(img_levels, btn_size)

        img_restart = pygame.image.load(os.path.join(self.img_path, "restart.png")).convert_alpha()
        self.btn_restart = pygame.transform.smoothscale(img_restart, btn_size)

        img_next = pygame.image.load(os.path.join(self.img_path, "nextlevel.png")).convert_alpha()
        self.btn_next = pygame.transform.smoothscale(img_next, btn_size)

        # LAYOUTING
        self.overlay_rect = pygame.Rect(0, 0, 500, 300)
        self.overlay_rect.center = (self.width // 2, self.height // 2) #ini box overlay

        y_pos = self.overlay_rect.centery + 50
        spacing = 130 #layout tombol
        
        self.rect_levels = self.btn_levels.get_rect(center=(self.overlay_rect.centerx - spacing, y_pos))
        self.rect_restart = self.btn_restart.get_rect(center=(self.overlay_rect.centerx, y_pos))
        self.rect_next = self.btn_next.get_rect(center=(self.overlay_rect.centerx + spacing, y_pos))

    def draw(self, status_text, color):
        # shading bg gelap
        overlay_bg = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        overlay_bg.fill((0, 0, 0, 150)) 
        self.screen.blit(overlay_bg, (0, 0))

        # gambar kotak menu (Abu-abu)
        pygame.draw.rect(self.screen, (80, 80, 80), self.overlay_rect, border_radius=20)
        # Opsional: Tambah outline putih tipis agar lebih manis
        pygame.draw.rect(self.screen, (200, 200, 200), self.overlay_rect, width=2, border_radius=20)

        # status
        font = pygame.font.SysFont("Arial", 45, bold=True)
        text_surf = font.render(status_text, True, color)
        text_rect = text_surf.get_rect(center=(self.overlay_rect.centerx, self.overlay_rect.top + 70))
        self.screen.blit(text_surf, text_rect)

        # gambar
        self.screen.blit(self.btn_levels, self.rect_levels)
        self.screen.blit(self.btn_restart, self.rect_restart)
        self.screen.blit(self.btn_next, self.rect_next)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect_levels.collidepoint(event.pos):
                return "PICK_LEVEL"
            if self.rect_restart.collidepoint(event.pos):
                return "RESTART"
            if self.rect_next.collidepoint(event.pos):
                return "NEXT"
        return None