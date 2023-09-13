import unittest

from src.models.stats import Stats

class TestStats(unittest.TestCase):
    def test_creation(self):
        stats = Stats(armor=10,attack=15,move_speed=5)
        self.assertEquals(10,stats.armor)
        self.assertEquals(15,stats.attack)
        self.assertEquals(5,stats.move_speed)
if __name__=="__main__":
    unittest.main()