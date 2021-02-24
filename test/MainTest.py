import unittest

from src.main import print_hi


class MainTest(unittest.TestCase):

    def test_print(self):
        self.assertEqual(print_hi("name"), "Hi, name")