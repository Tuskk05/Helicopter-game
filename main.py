import pygame
from game import Game
from screen import Screen
from factorySprites import FactorySprites
from bird import Bird
from cloud import Cloud
from umbrella import Umbrella
from mountain import Mountain

# Initialize PyGame
# setup for sounds_music, defaults are good
pygame.mixer.init()
pygame.init()
# Screen object creation
screen = pygame.display.set_mode((Screen.width, Screen.height))

# Chose difficulty level
level = 'difficult'

if level == 'easy':
    factory_flying = FactorySprites([Bird(), Umbrella()],[300, 600], pygame.USEREVENT + 1)
    factory_landscape = FactorySprites([Cloud(), Mountain()], [500, 2000], pygame.USEREVENT + 10)
elif level == 'difficult':
    factory_flying = FactorySprites([Bird(), Umbrella()],
                                    [400, 800],
                                    pygame.USEREVENT + 1)
    factory_landscape = FactorySprites([Cloud(), Mountain()], [500, 2000],
                                       pygame.USEREVENT + 10)

# play
game = Game(factory_flying, factory_landscape)
game.play()