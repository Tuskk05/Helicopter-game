import pygame
import random
from pygame.locals import RLEACCEL
from screen import Screen
from gameSprite import GameSprite

class Jet(GameSprite):
    Min_Speed = 7
    Max_Speed = 12

    def __init__(self):
        super().__init__()
        self.surf = pygame.image.load("icons/jet.png").convert()
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        # Starts at a random position at the top
        self.rect = self.surf.get_rect(
            center=(
                random.randint(Screen.width + 20, Screen.width + 100),
                random.randint(0, Screen.height // 2)
            )
        )
        self.speed = random.randint(self.Min_Speed, self.Max_Speed)

    def update(self):
        # Moves vertically at a constant speed
        self.rect.move_ip(-self.speed, 0)
        if self.rect.top > Screen.height:
            self.kill()

    def clone(self):
        return Jet()