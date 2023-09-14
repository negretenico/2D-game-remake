from src.sprite.sprite import Sprite
from src.models.point import Point
from src.models.stats import Stats


class Player:
    def __init__(self,position:Point,image:str):
        self.sprite = Sprite(point=position,image_path=image)
        self.stats = Stats(armor=100,attack=5,move_speed=1)
        self.position = position
    def get_sprite_image(self):
        return self.sprite.get_image()
    def get_position(self)->Point:
        return (self.position.x,self.position.y)
    def move_left(self)->None:
        self.sprite.move_horizontal(self.stats.move_speed)
        self.position = Point(self.position.x-self.stats.move_speed,self.position.y)
    def move_right(self)->None:
        self.sprite.move_horizontal(-self.stats.move_speed)
        self.position = Point(self.position.x+self.stats.move_speed,self.position.y)
    def jump(self)->None:
        pass
    def croutch(self)->None:
        pass