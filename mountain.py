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
        # Comença a la part de baix de la pantalla (paisatge)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(Screen.width + 20, Screen.width + 100),
                random.randint(int(Screen.height * 0.8), Screen.height - 10)
            )
        )
        self.speed = random.randint(self.Min_Speed, self.Max_Speed)

    def update(self):
        # Es mou horitzontalment cap a l’esquerra, com un núvol però a baix
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

    def clone(self):
        return Mountain()