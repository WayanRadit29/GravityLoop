import pygame
from src.ui.lobby import Lobby
from src.core.game_engine import GameEngine

def main():
    pygame.init()
    # Gunakan clock untuk mengatur FPS agar tidak membebani CPU
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Gravity Loop")
    
    lobby = Lobby(screen)

    running = True
    show_lobby = True # Flag untuk mengontrol kapan lobby berhenti

    while running:
        # 1. Event Handling
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                return # Langsung keluar dari fungsi
        
            # Cek klik tombol di lobby
            if show_lobby:
                action = lobby.handle_event(event)
                if action == "START":
                    show_lobby = False # Berhenti looping lobby
                    running = False    # Keluar dari loop lobby untuk masuk ke GameEngine

        # 2. Drawing (Harus di dalam WHILE)
        if show_lobby:
            lobby.draw()
            pygame.display.flip()
        
        # Limit 60 FPS
        clock.tick(60)

    # Setelah loop lobby selesai (tombol start diklik), jalankan GameEngine
    game = GameEngine()
    game.run()

    pygame.quit()

if __name__ == "__main__":
    main()