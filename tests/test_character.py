from unittest import TestCase
from levelup.character import Character

class TestCharacterInitWithName(TestCase):
    def test_init(self):
        ARBITRARY_NAME = "MyName"
        testobj = Character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobj.name)

class TestCharacterInitWithoutName(TestCase):
    def test_init(self):
        ARBITRARY_NAME = " "
        testobj = Character(ARBITRARY_NAME)
        self.assertNotEqual(ARBITRARY_NAME, testobj.name)

class TestChracterEnterMap(TestCase):
    def test_init(self):
        ARBITRARY_NAME = ""
        testobj = enter_map(gamemap())
        self.assertNotEqual(None, testobj.map)

class TestCharacterGetPosition(TestCase):
    def test_init(self):
        ARBITRARY_NAME = ""
        testobj = Character(ARBITRARY_NAME)
        self.assertNotEqual(Name, testobj.position)

class TestCharacterMove(TestCase):
    def test_init(self):
        ARBITRARY_NAME = ""
        testobj = Character(ARBITRARY_NAME)
        self.assertNotEqual(None, testobj.move("n"))
