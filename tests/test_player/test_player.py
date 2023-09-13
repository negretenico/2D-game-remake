import unittest
from src.models.point import Point
from src.player.player import Player
class TestPlayer(unittest.TestCase):
    def test_creation(self):
        player = Player(position=Point(0,0),image="assets\\images\\back_ground.png")
        self.assertEquals((0,0),player.get_position())
        self.assertIsNotNone(player.get_sprite_image())
        
if __name__ =="__main__":
    unittest.main()