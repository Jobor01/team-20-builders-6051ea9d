from unittest import TestCase
from levelup.character import Character

class TestCharacterInitWithName(TestCase):
    def test_init(self):
        ARBITRARY_NAME = "MyName"
        testobj = Character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobj.name)

class TestCharacterInitNoName(TestCase):
    def test_init(self):
        ARBITRARY_NAME = " "
        testobj = Character(ARBITRARY_NAME)
        self.assertNotEqual(ARBITRARY_NAME, testobj.name)
