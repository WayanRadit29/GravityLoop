import pygame

def load_sprite(path, scale=None):
    try:
        image = pygame.image.load(path).convert_alpha()
        if scale:
            image = pygame.transform.smoothscale(image, scale)
        return image
    except Exception as e:
        print(f"[SPRITE LOAD FAILED] {path} | {e}")
        return None
