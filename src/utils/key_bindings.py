from src.player.player import Player
import pygame 
from typing import Dict
class KeyBindings:
    def __init__(self, player:Player):
        self.key_bindings:Dict[int,callable] ={
            pygame.K_LEFT: player.move_left(),
            pygame.K_RIGHT: player.move_right(),
            pygame.K_UP: player.jump(),
            pygame.K_DOWN: player.croutch()
        }
    def get_key_bindings(self)-> Dict[int,callable]:
        return self.key_bindings