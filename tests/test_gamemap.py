from unittest import TestCase
from levelup.gamemap import gamemap
from levelup.position import position


class TestTotalPositions(TestCase):
    def test_init(self):
        num_position = 100
        testobj = gamemap(num_position)
        self.assertEqual(num_position, testobj.num_position)

class TestPositions(TestCase):
    def test_init(self):
        testobj = gamemap(100)
        self.assertNotEqual(None,testobj.position)

class TestCalculatePositionBasedOnDirection(TestCase):
    def test_init(self):
        testobj = gamemap(100)
        direction = 'n'
        startpos = testobj.position [4][5]
        endpos = testobj.calculate_position(startpos, direction)
        self.assertEqual(endpos.x , 5)
        self.assertEqual(endpos.y , 5)

class TestWalls(TestCase):
    def test_init(self):
        testobj = gamemap(100)
        direction = "e"
        startpos = testobj.position[4][9]
        endpos = testobj.calculate_position(startpos, direction)
        self.assertEqual(endpos.y, 4)
        self.assertEqual(endpos.x ,9)
