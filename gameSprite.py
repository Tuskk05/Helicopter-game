import pygame
from abc import ABC, abstractmethod

class GameSprite(pygame.sprite.Sprite, ABC):
    """
    Classe base abstracta per a tots els sprites del joc.
    Defineix la interfície comuna (Prototype) que obliga
    les subclasses a implementar el mètode clone().
    """
    def __init__(self):
        super().__init__()

    @abstractmethod
    def clone(self):
        """
        Retorna una nova instància (còpia) de la subclasse concreta.
        Cada subclasse (Bird, Cloud, etc.) ha d'implementar aquest mètode.
        """
        pass
