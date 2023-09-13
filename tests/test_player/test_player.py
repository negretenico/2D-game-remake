import unittest
from src.models.point import Point
from src.player.player import Player
class TestPlayer(unittest.TestCase):
    def test_creation(self):
        player = Player(position=Point(0,0),image="assets\\images\\back_ground.png")
        self.assertEquals((0,0),player.get_position())
        self.assertIsNotNone(player.get_sprite_image())
    def test_moves_left(self):
        player = Player(position=Point(0,0),image="assets\\images\\back_ground.png")
        player.move_left()
        self.assertGreater(player.position.x,0)
    def test_move_right(self):
        player = Player(position=Point(0,0),image="assets\\images\\back_ground.png")
        player.move_right()
        self.assertLess(player.position.x,0)
    def test_jump(self):
        pass
    def test_croutch(self):
        pass
if __name__ =="__main__":
    unittest.main()