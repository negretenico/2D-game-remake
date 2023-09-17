import unittest
from src.player.player import Player
from typing import Dict
from src.utils.key_bindings import KeyBindings
from unittest.mock import Mock, patch
from pygame import Surface
class TestUtils(unittest.TestCase):
    @patch("pygame.image.load",return_value=Surface((1,1)))
    def test_can_get(self,mock_load):
        key_bindings:Dict[int,callable] = KeyBindings(player=Player(None,None)).get_key_bindings()
        self.assertTrue(len(key_bindings)!=0)

if __name__ =="__main__":
    unittest.main()