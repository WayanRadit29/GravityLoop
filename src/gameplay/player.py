import pygame 

class Player:
    def __init__(self, x : float, y : float):
        # Posisi (float)
        self.x = x
        self.y = y

        # Kecepatan
        self.vx = 0.0
        self.vy = 0.0

        # akselerasi
        self.ax = 0.0
        self.ay = 0.0


        
    def update(self):
        '''
        Update player berdasarkan konsep hukum mekanika Newton

        '''

        # Update kecepatan dari akselerasi
        self.vx += self.ax
        self.vy += self.ay

        # Update posisi dari kecepatan
        self.x += self.vx
        self.y += self.vy

        # Reset akselerasi
        self.ax = 0.0
        self.ay = 0.0

    def apply_force(self, fx: float, fy: float):
        '''
        Apply force kepada player (contoh forcenya dari planet nanti)
        '''

        self.ax += fx
        self.ay += fy
        

    def render(self, surface: pygame.Surface):
        pass


