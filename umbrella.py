import pygame
import random
from pygame.locals import RLEACCEL
from screen import Screen
from gameSprite import GameSprite

class Umbrella(GameSprite):
    Min_Speed = 3
    Max_Speed = 7

    def __init__(self):
        super().__init__()
        self.surf = pygame.image.load("icons/umbrella.png").convert()
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        # Comença a una posició aleatòria a la part superior
        self.rect = self.surf.get_rect(
            center=(random.randint(0, Screen.width), -20)
        )
        self.speed = random.randint(self.Min_Speed, self.Max_Speed)

    def update(self):
        # Es mou cap avall amb una velocitat vertical constant
        self.rect.move_ip(0, self.speed)
        if self.rect.top > Screen.height:
            self.kill()

    def clone(self):
        return Umbrella()