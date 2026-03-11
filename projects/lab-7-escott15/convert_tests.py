import unittest
from convert import *


class TestConvert(unittest.TestCase):
    def test_str_to_float1(self):
        self.assertEqual(str_to_float("1.2"), 1.2)
    def test_str_to_float2(self):
        self.assertEqual(str_to_float("6.7"), 6.7)
