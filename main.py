from src.player.player import Player
import pygame 
import sys 
from typing import Final
import os
from src.models.point import Point
from src.sound.music_manager import MusicManager
from src.sprite.animation_manager import AnimationManager
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
music = 'assets\\sound\\music\\music.mp3'
player = Player(position=inital_point,image=idle)
key_bindings = KeyBindings(player=player)
music_manager = MusicManager()
animation_manager = AnimationManager()
bindings = key_bindings.get_key_bindings()
music_manager.load(music)
music_manager.change_volume(.5)
music_manager.play()
animation_manager.add_animation('move_right',[os.path.join('assets\\images\\Zetterburn\\zet_run',i)for i in os.listdir('assets\\images\\Zetterburn\\zet_run')],len(os.listdir('assets\\images\\Zetterburn\\zet_run')))
animation_manager.add_animation('idle',[os.path.join('assets\\images\\Zetterburn\\zet_idle_new',i)for i in os.listdir('assets\\images\\Zetterburn\\zet_idle_new')],len(os.listdir('assets\\images\\Zetterburn\\zet_idle_new')))

animation_manager.set_current_animation('idle')
# Initialize key state dictionary
key_state = {
    pygame.K_RIGHT: False,
}

while True:
    clock.tick(60)
    screen.blit(bg, (0, 0))

    # Update key state continuously
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            key_state[event.key] = True
        elif event.type == pygame.KEYUP:
            key_state[event.key] = False

    # Check the state of keys and update player accordingly
    if key_state[pygame.K_RIGHT]:
        key_bindings.get_key_bindings().get(pygame.K_RIGHT,print)()
        if(animation_manager.get_name()!='move_right'):
            animation_manager.set_current_animation('move_right')
    else:
        if(animation_manager.get_name()!='idle'):
            animation_manager.set_current_animation('idle')

    # Update animation and screen
    animation_manager.update()
    screen.blit(animation_manager.get_current_frame(), player.get_position())

    pygame.display.update()

# while True:
#     clock.tick(60)
#     screen.blit(bg,(0,0))
#     animation_manager.set_current_animation('idle')
#     screen.blit(animation_manager.get_current_frame(),player.get_position())
#     for event in pygame.event.get():
#         if(event.type==pygame.KEYDOWN):
#             bindings.get(event.key,print)()
#             animation_manager.set_current_animation('move_right')
#             animation_manager.update()
#             pygame.display.update()
#     animation_manager.update()
#     pygame.display.update()
