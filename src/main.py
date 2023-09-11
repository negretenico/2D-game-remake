import pygame 
import sys 
from typing import Final 
SCREEN_WIDTH: Final = 1280
SCREEN_HEIGHT: Final = 720 

clock = pygame.time.Clock()
pygame.init()
bg = pygame.image.load("assets\images\\back_ground.png")
bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

while True:
    clock.tick(60)
    screen.blit(bg,(0,0))
    pygame.display.update()