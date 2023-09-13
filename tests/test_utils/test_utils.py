import unittest
from src.player.player import Player
from typing import Dict
from src.utils.key_bindings import KeyBindings
class TestUtils(unittest.TestCase):
    def test_can_get(self):
        key_bindings:Dict[int,callable] = KeyBindings(player=Player(None,None))
        self.assertTrue(len(key_bindings)!=0)

if __name__ =="__main__":
    unittest.main()