import unittest
from group import groupsof3

class testCases(unittest.TestCase): #test cases for group.groupsof3 function to ensure it is working properly. 
    def test_groupsof3_1(self):
        input = []
        result = groupsof3(input)
        expected = []
        self.assertEqual(expected, result)
    def test_groupsof3_2(self):
        expected = [[1,2,3]]
        input = [1, 2, 3]
        result = groupsof3(input)
        self.assertEqual(expected, result)
    def test_groupsof3_3(self):
        input = [1, 2, 3, 4, 5, 6, 7]
        expected = [[1,2,3], [4,5,6], [7]] 
        result = groupsof3(input)
        self.assertEqual(expected, result)
    def testgroupsof3_4 (self):
        input = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
        expected = [[10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]]
        result = groupsof3(input)
        self.assertEqual(expected, result)
    def testgroupsof3_5 (self):
        input = [9, 8, 7, 6, 5]
        expected = [[9, 8, 7], [6, 5]]
        result =groupsof3(input)
        self.assertEqual(expected, result)



if __name__ == '__main__':
    unittest.main()

