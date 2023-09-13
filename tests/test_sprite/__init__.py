import unittest

from src.sprite.sprite import Sprite
from src.models.point import Point
class TestSprite(unittest.TestCase):
    def test_creation(self):
        sprite = Sprite(point=Point(0,0),image_path="assets\\images\\back_ground.png")
        self.assertIsNotNone(sprite.get_image())
        self.assertIsNotNone(sprite.get_image_rect())
if __name__ =="__main__":
    unittest.main()