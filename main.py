import pygame
from game import Game
from screen import Screen
from factorySprites import FactorySprites
from bird import Bird
from cloud import Cloud
from umbrella import Umbrella
from mountain import Mountain
from jet import Jet
from missile import Missile

# Initialize PyGame
# setup for sounds_music, defaults are good
pygame.mixer.init()
pygame.init()
# Screen object creation
screen = pygame.display.set_mode((Screen.width, Screen.height))

# Choose difficulty level
level = 'easy'

if level == 'easy':
    factory_flying = FactorySprites([Bird(), Umbrella(), Jet(), Missile()],[1500, 2000, 2000, 3000], pygame.USEREVENT + 1)
    factory_landscape = FactorySprites([Cloud(), Mountain()], [1000, 5000], pygame.USEREVENT + 10)
elif level == 'difficult':
    factory_flying = FactorySprites([Bird(), Umbrella(), Jet(), Missile()], [800, 1200, 1200, 1800], pygame.USEREVENT + 1)
    factory_landscape = FactorySprites([Cloud(), Mountain()], [1000, 5000], pygame.USEREVENT + 10)

# play
game = Game(factory_flying, factory_landscape)
game.play()