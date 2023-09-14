from src.player.player import Player
import pygame 
import sys 
from typing import Final
import pprint
from src.models.point import Point
from src.utils.key_bindings import KeyBindings 
SCREEN_WIDTH: Final = 1280
SCREEN_HEIGHT: Final = 720 

clock = pygame.time.Clock()
pygame.init()
bg = pygame.image.load("assets\images\\back_ground.png")
bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
inital_point = Point(SCREEN_WIDTH//2,SCREEN_HEIGHT//2)
idle = 'assets\\images\\Zetterburn\\zet_idle_new\\zet_idle_new_0.png'
player = Player(position=inital_point,image=idle)
key_bindings = KeyBindings(player=player)
bindings = key_bindings.get_key_bindings()
while True:
    clock.tick(60)
    screen.blit(bg,(0,0))
    screen.blit(player.get_sprite_image(),player.get_position())
    pygame.display.update()
    for event in pygame.event.get():
        if(event.type==pygame.KEYDOWN):
            bindings.get(event.key)()