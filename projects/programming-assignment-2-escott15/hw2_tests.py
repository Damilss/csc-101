import data
import hw2
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle1(self):
        itv1 = data.Point(0, 10)
        itv2 = data.Point(10, 0)
        expected = data.Rectangle(data.Point(0,10), data.Point(10,0))
        self.assertEqual(expected, hw2.create_rectangle(itv1, itv2))
    def test_create_rectangle2(self):
        itv3 = data.Point(10, 0)
        itv4 = data.Point(0, 10)
        expected = data.Rectangle(data.Point(0, 10), data.Point(10, 0))
        self.assertEqual(expected, hw2.create_rectangle(itv3, itv4))
    # Part 2
    def test_shorter_duration_than1(self):
        itv5 = data.Duration(3, 20)
        itv6= data.Duration(4, 0)
        expected = True
        self.assertEqual(expected, hw2.shorter_duration_than(itv5, itv6))
    def test_shorter_duration_than2(self):
        itv7 = data.Duration(5, 50)
        itv8 = data.Duration(5, 30)
        expected = False
        self.assertEqual(expected, hw2.shorter_duration_than(itv7, itv8))
    # Part 3
    def test_songs_shorter_than1(self):
        bound = data.Duration(4, 0)
        lst = [
            data.Song("Adele", "Hello", data.Duration(6, 7)),
            data.Song("Taylor Swift", "Lover", data.Duration(3, 45)),
            data.Song("Ed Sheeran", "Perfect", data.Duration(4, 0)),
            data.Song("Bruno Mars", "Treasure", data.Duration(3, 0))
        ]
        expected = [
            data.Song("Taylor Swift", "Lover", data.Duration(3, 45)),
            data.Song("Bruno Mars", "Treasure", data.Duration(3, 0))
        ]
        self.assertEqual(expected, hw2.songs_shorter_than(lst, bound))
    def test_songs_shorter_than2(self):
        bound = data.Duration(3, 30)
        lst = [
            data.Song("Adele", "Easy On Me", data.Duration(3, 45)),
            data.Song("Ed Sheeran", "Shivers", data.Duration(4, 5)),
            data.Song("Olivia Rodrigo", "Drivers License", data.Duration(4, 2))
        ]
        expected = None
        self.assertEqual(expected, hw2.songs_shorter_than(lst, bound))
    # Part 4
    def test_running_time1(self):
        lst = [
            data.Song("Ed Sheeran", "Perfect", data.Duration(4, 23)),
            data.Song("Coldplay", "Yellow", data.Duration(4, 29)),
            data.Song("Billie Eilish", "Ocean Eyes", data.Duration(3, 20))
        ]
        bound = [1, 2, 3]
        expected = data.Duration(12, 12)
        self.assertEqual(expected, hw2.running_time(lst, bound))
    def test_running_time2(self):
        lst = [
            data.Song("Adele", "Hello", data.Duration(6, 7)),
            data.Song("Taylor Swift", "Lover", data.Duration(3, 45)),
            data.Song("Bruno Mars", "Treasure", data.Duration(3, 0))
        ]
        bound = [1,2]
        expected = data.Duration(9, 52)
        self.assertEqual(expected, hw2.running_time(lst, bound))
    # Part 5
    def test_validate_route1(self):
        route = ['san francisco', 'palo alto']
        assert hw2.validate_route(hw2.city_links, route) is False
    def test_validate_route2(self):
        route = ['san luis obispo', 'santa margarita', 'atascadero']
        assert hw2.validate_route(hw2.city_links, route) is True


    # Part 6
    def test_longest_repetition1(self):
        itv11 = [1, 1, 2, 2, 2, 3, 3]
        expected = 2
        self.assertEqual(expected, hw2.longest_repetition(itv11))
    def test_longest_repetition2(self):
        itv12 = [4, 4, 5, 5]
        expected = 0
        self.assertEqual(expected, hw2.longest_repetition(itv12))
    def test_longest_repetition3(self):
        itv13 = []
        assert hw2.longest_repetition(itv13) is None

if __name__ == '__main__':
    unittest.main()

