import data
import lab5
import unittest
import math
# Write your test cases for each part below.
class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.
    # Part 2
    #    Part 2 tests should be in data_tests.py.
    # Part 3
    def test_time_add1(self):
        time1 = data.Time(4, 19, 45)
        time2 = data.Time(4, 19, 45)
        expected = data.Time(8, 39, 30)
        self.assertEqual(lab5.time_add(time1, time2), expected)
    def test_time_add2(self):
        time1 = data.Time(4, 53, 0)
        time2 = data.Time(4, 10, 27)
        expected  = data.Time(9, 3, 27)
        self.assertEqual(lab5.time_add(time1, time2), expected)
    # Part 4
    def test_is_descending1(self):
        input1 = [10.0, 8.0, 5.0, 2.0]
        expected = True
        self.assertEqual(lab5.is_descending(input1), expected)
    def test_is_descending2(self):
        input1 = [10.0, 12.0, 5.0, 2.0]
        expected = False
        self.assertEqual(lab5.is_descending(input1), expected)
    # Part 5
    def test_largest_between1(self):
        l1 = [1 , 5, 10, 15, 20]
        lower1 = 5
        upper1 = 18
        expected = 15
        self.assertEqual(lab5.largest_between(l1, upper1, lower1), expected)
    def test_largest_between2(self):
        l2 = [1, 2, 3, 4]
        lower2 = 10
        upper2 = 20
        expected = None
        self.assertEqual(lab5.largest_between(l2, upper2, lower2), expected)
    # Part 6
    def test_furthest_from_origin1(self):
        input1 = [
            data.Point(1,2),
            data.Point(2,3),
            data.Point(3,4)
        ]
        expected = data.Point(3, 4)
        self.assertEqual(lab5.furthest_from_origin(input1), expected)
    def test_furthest_from_origin2(self):
        input1 = [
            data.Point(5, 12),
            data.Point(8, 15)
        ]
        expected = data.Point(8, 15)
        self.assertEqual(lab5.furthest_from_origin(input1), expected)
if __name__ == '__main__':
    unittest.main()