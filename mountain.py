import pygame
import random
from pygame.locals import RLEACCEL
from screen import Screen
from gameSprite import GameSprite

class Mountain(GameSprite):
    Min_Speed = 2
    Max_Speed = 5

    def __init__(self):
        super().__init__()
        self.surf = pygame.image.load("icons/mountain.png").convert()
        self.surf.set_colorkey((0, 0, 0), pygame.RLEACCEL)
        # Starts at the botton of the screen
        self.rect = self.surf.get_rect()
        self.rect.left = random.randint(Screen.width + 20, Screen.width + 100)
        self.rect.bottom = Screen.height
        self.speed = 3

    def update(self):
        # Moves like a cloud but in the lower part of the screen
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

    def clone(self):
        return Mountain()