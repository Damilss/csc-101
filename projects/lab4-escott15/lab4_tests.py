import data
import unittest
import lab4



# Write your test cases for each part below.
class TestCases(unittest.TestCase):
    #part 1
    def test_first_element_1(self):
        input = [[1, 2], [3, 4]]
        result1 = lab4.first_element(input)
        expected1 = [1, 3]
        self.assertEqual(result1, expected1)

    def test_first_element_2(self):
        input = [[9, 8], [7, 6]]
        result1 = lab4.first_element(input)
        expected1 = [9, 7]
        self.assertEqual(result1, expected1)
    #part 2
    def test_ (self):
        input = [data.Point(1,2), data.Point(3,4)]
        result1 = lab4.x_coordinates(input)
        expected1 = [1, 3]
        self.assertEqual(result1, expected1)

    def test_part2_1(self):
        input = [data.Point(7,2), data.Point(9,4)]
        result1 = lab4.x_coordinates(input)
        expected1 = [7, 9]
        self.assertEqual(result1, expected1)
    #part 3
    def test_part3(self):
        input = [data.Point(1,2), data.Point(3,4), data.Point(-3,5), data.Point(-4,9)]
        result = lab4.are_in_positive_quadrant(input)
        expected1 = [data.Point(1,2), data.Point(3,4)]
        self.assertEqual(result, expected1)
    #part 4
    def test_eudistance(self):
        input1 = data.Point(1, 2)
        input2 = data.Point(3, 4)
        expected = 2.8
        self.assertAlmostEqual(lab4.eudistance(input1, input2), expected, places=1)
    def test_eudistance1(self):
        input1 = data.Point(4, 6)
        input2 = data.Point(0, 0)
        expected =7.211
        self.assertAlmostEqual(lab4.eudistance(input1, input2), expected, places=1)
    #part 5
    def test_mandistance(self):
        input1 = data.Point(1, 2)
        input2 = data.Point(3, 4)
        expected = 2.8
        self.assertAlmostEqual(lab4.eudistance(input1, input2), expected, places=1)
    def test_mandistance(self):
        input1 = data.Point(1, 2)
        input2 = data.Point(3, 4)
        expected = 4
        self.assertAlmostEqual(lab4.manhattandistance(input1,input2), expected)
    #part 6
    def test_d(self):
        input1 = [data.Point(1,2), data.Point(3,4)]
        expected =[2.23607,5]
        result = lab4.d(input1)
        for i in range(len(result)):
            self.assertAlmostEqual(result[i], expected[i], places=1)

if __name__ == '__main__':
    unittest.main()

