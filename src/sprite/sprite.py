from src.models.point import Point
import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self,point:Point,image_path: str):
        super().__init__()
        self.point =point
        self.__image =  pygame.image.load(image_path)
        self.__image_ret = self.__image.get_rect()
    def get_image(self):
        return self.__image
    def get_image_rect(self):
        return self.__image_ret
    def move_horizontal(self,magnitude):
        self.__image_ret.x +=magnitude
