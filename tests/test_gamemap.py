from unittest import TestCase
from levelup.gamemap import gamemap
from levelup.position import position


class TestTotalPositions(TestCase):
        def test_init(self):
            num_postions = 100
            testobj = gamemap(num_postion)
            self.assertEqual(num_postion, testobj.num_postion)

class TestPositions(TestCase):
    def test_init(self):
        testobj = gamemap(100)
        self.assertNotEqual(None,testobj.position)

class TestCalculatePostionBasedOnDirection(TestCase):
    def test_init(self):
        testobj = gamemap(100)
        direction = 'n'
        startpos = testobj.position[4][5]
        endpos = testobj.calculated_position(startpos, direction)
        self.assertEquals(endpos.x , 5)
        self.assertEquals(endpos.y , 5)

class TestWalls(TestCase):
    def test_init(self):
        testobj = gamemap(100)
        direction = "e"
        startpos = testobj.position[4][9]
        endpos = testobj.calculated_position(startpos, direction)
        self.assertEquals(endpos.y, 4)
        self.assertEquals(endpos.x ,9)
