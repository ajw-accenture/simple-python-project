import unittest
from hello_world.hello_world import HelloWorld

class TestHelloWorld(unittest.TestCase):
    def test_thing(self):
        expected = 'Hello, world!'
        actual = HelloWorld.say()
        self.assertEqual(actual, expected)
