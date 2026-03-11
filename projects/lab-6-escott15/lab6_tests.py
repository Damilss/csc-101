import data
import lab6
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
    def test_sort_books_normal(self):
        expected = [
            data.Book("1984", "George Orwell", 1949),
            data.Book("A Tale of Two Cities", "Charles Dickens", 1859),
            data.Book("Animal Farm", "George Orwell", 1945),
            data.Book("Brave New World", "Aldous Huxley", 1932),
            data.Book("Crime and Punishment", "Fyodor Dostoevsky", 1866),
            data.Book("Fahrenheit 451", "Ray Bradbury", 1953),
            data.Book("Jane Eyre", "Charlotte Brontë", 1847),
            data.Book("Moby-Dick", "Herman Melville", 1851),
            data.Book("Pride and Prejudice", "Jane Austen", 1813),
            data.Book("The Catcher in the Rye", "J.D. Salinger", 1951),
            data.Book("The Great Gatsby", "F. Scott Fitzgerald", 1925),
            data.Book("The Hobbit", "J.R.R. Tolkien", 1937),
            data.Book("To Kill a Mockingbird", "Harper Lee", 1960),
            data.Book("Wuthering Heights", "Emily Brontë", 1847),
        ]
        books = [
            data.Book("The Catcher in the Rye", "J.D. Salinger", 1951),
            data.Book("To Kill a Mockingbird", "Harper Lee", 1960),
            data.Book("1984", "George Orwell", 1949),
            data.Book("Brave New World", "Aldous Huxley", 1932),
            data.Book("Moby-Dick", "Herman Melville", 1851),
            data.Book("A Tale of Two Cities", "Charles Dickens", 1859),
            data.Book("Pride and Prejudice", "Jane Austen", 1813),
            data.Book("The Great Gatsby", "F. Scott Fitzgerald", 1925),
            data.Book("The Hobbit", "J.R.R. Tolkien", 1937),
            data.Book("Fahrenheit 451", "Ray Bradbury", 1953),
            data.Book("Animal Farm", "George Orwell", 1945),
            data.Book("Crime and Punishment", "Fyodor Dostoevsky", 1866),
            data.Book("Jane Eyre", "Charlotte Brontë", 1847),
            data.Book("Wuthering Heights", "Emily Brontë", 1847),
        ]
        lab6.selection_sort_books(books)
        self.assertEqual(expected, books)

    def test_sort_books_small(self):
        expected = [
            data.Book("Alpha", "Greg Rucka", 2010),
            data.Book("Delta", "Tony Park", 2018),
            data.Book("Zoo", "James Patterson", 2012),
        ]
        result = small_books = [
            data.Book("Zoo", "James Patterson", 2012),
            data.Book("Alpha", "Greg Rucka", 2010),
            data.Book("Delta", "Tony Park", 2018),
        ]
        lab6.selection_sort_books(result)
        self.assertEqual(expected, result)

    # Part 2
    def test_swap_case1(self):
        expected = ""
        result =lab6.swap_case("")
        self.assertEqual(expected, result)
    def test_swap_case2(self):
        result = "Hello, Wörld!"
        expected = "hELLO, wÖRLD!"
        self.assertEqual(expected, lab6.swap_case(result))
    # Part 3
    def test_str_translate1(self):
        expected = "xbcdcbx"
        result = lab6.str_translate("abcdcba", 'a', 'x')
        self.assertEqual(expected, result)
    def test_str_translate2(self):
        expected = 'hello'
        result = lab6.str_translate("hello", 'a', 'x')
        self.assertEqual(expected, result)

    # Part 4

    def test_histrogram1(self):
        expected = {}
        result = lab6.histogram("")
        self.assertEqual(expected, result)
    def test_histrogram2(self):
        result = lab6.histogram("cat dog cat bird cat")
        expected = {"cat": 3, "dog": 1, "bird": 1}
        self.assertEqual(expected, result)



if __name__ == '__main__':
    unittest.main()
