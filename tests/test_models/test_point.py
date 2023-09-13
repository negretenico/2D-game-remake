import unittest

from src.models.point import Point
class TestPoint(unittest.TestCase):
    def test_creation(self):
        point = Point(0,0)
        self.assertEquals(0,point.x)
        self.assertEquals(0,point.y)
if __name__ =="__main__":
    unittest.main()