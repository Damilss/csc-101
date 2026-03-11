import data
import hw1
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count1(self):
        itv1 = ("burger") # inputted test value 1
        expected = 2
        self.assertEqual(hw1.vowel_count(itv1), expected)

    def test_vowel_count2(self):
        itv2 = ("waffle")
        expected = 2
        self.assertEqual(hw1.vowel_count(itv2), expected)
    # Part 2
    def test_short_lists1(self):
        itv3 = [[2, 3], [4, 5], [5, 7, 8, 9],[1]]
        expected = [[2, 3], [4, 5]]
        self.assertEqual(hw1.short_lists(itv3), expected)
    def test_short_lists2(self):
        itv4 = [[2, 5, 7], [6,7], [5, 7, 8, 9]]
        expected = [[6, 7]]
        self.assertEqual(hw1.short_lists(itv4), expected)

    # Part 3
    def test_ascending_pairs1(self):
        itv5 = [[2, 5, 7], [7, 6], [5, 7, 8, 9]]
        expected = [[2, 5, 7], [6, 7], [5, 7, 8, 9]]
        self.assertEqual(hw1.ascending_pairs(itv5), expected)
    def test_ascending_pairs2(self):
        itv6 = [[6, 7, 8], [2, 1], [4, 1, 6, 7],[41,40]]
        expected = [[6, 7, 8], [1, 2], [4, 1, 6, 7],[40, 41]]
        self.assertEqual(hw1.ascending_pairs(itv6), expected)

    # Part 4
    def test_add_prices1(self):
        itv7 = [data.Price(44,22), data.Price(22, 42)]
        expected = data.Price(66,64)
        self.assertEqual(hw1.add_prices(itv7), expected)
    def test_add_prices2(self):
        itv8 = [data.Price(67, 67), data.Price(68, 68)]
        expected = data.Price(136, 35)



    # Part 5
    def test_rectangle_area1(self):
        itv9 = data.Rectangle(data.Point(0,0),data.Point(4, 8))
        expected = 32
        self.assertEqual(hw1.rectangle_area(itv9), expected)
    def test_rectangle_area2(self):
        itv10 = data.Rectangle(data.Point(0,0),data.Point(6, 7))
        expected = 42
        self.assertEqual(hw1.rectangle_area(itv10), expected)
    # Part 6
    def test_books_by_author1 (self):
        test_catalog = [
            data.Book(["Patterson", "James"], "1st to Die"),
            data.Book(["Patterson", "James"], "5th Horseman"),
            data.Book(["King", "Stephen"], "It"),
            data.Book(["King", "Stephen"], "The Shining"),
            data.Book(["Rowling", "J.K."], "Harry Potter and the Philosopher's Stone"),
            data.Book(["Rowling", "J.K."], "Harry Potter and the Chamber of Secrets"),
            data.Book(["Tolkien", "J.R.R."], "The Hobbit"),
            data.Book(["Tolkien", "J.R.R."], "The Lord of the Rings"),
            data.Book(["Christie", "Agatha"], "Murder on the Orient Express"),
            data.Book(["Christie", "Agatha"], "And Then There Were None"),
            data.Book(["Martin", "George R.R."], "A Game of Thrones"),
            data.Book(["Martin", "George R.R."], "A Clash of Kings"),
            data.Book(["Collins", "Suzanne"], "The Hunger Games"),
            data.Book(["Collins", "Suzanne"], "Catching Fire"),
            data.Book(["Brown", "Dan"], "The Da Vinci Code"),
            data.Book(["Brown", "Dan"], "Angels & Demons"),
            data.Book(["Atwood", "Margaret"], "The Handmaid's Tale"),
            data.Book(["Orwell", "George"], "1984"),
            data.Book(["Orwell", "George"], "Animal Farm"),
            data.Book(["Shelley", "Mary"], "Frankenstein"),
        ]
        itv11 = "James Patterson"
        final_r = hw1.books_by_author(itv11, test_catalog)
        expected = ["1st to Die", "5th Horseman"]
        self.assertEqual(final_r, expected)
    def test_books_by_author2 (self) :
        test_catalog = [
            data.Book(["Patterson", "James"], "1st to Die"),
            data.Book(["Patterson", "James"], "5th Horseman"),
            data.Book(["King", "Stephen"], "It"),
            data.Book(["King", "Stephen"], "The Shining"),
            data.Book(["Rowling", "J.K."], "Harry Potter and the Philosopher's Stone"),
            data.Book(["Rowling", "J.K."], "Harry Potter and the Chamber of Secrets"),
            data.Book(["Tolkien", "J.R.R."], "The Hobbit"),
            data.Book(["Tolkien", "J.R.R."], "The Lord of the Rings"),
            data.Book(["Christie", "Agatha"], "Murder on the Orient Express"),
            data.Book(["Christie", "Agatha"], "And Then There Were None"),
            data.Book(["Martin", "George R.R."], "A Game of Thrones"),
            data.Book(["Martin", "George R.R."], "A Clash of Kings"),
            data.Book(["Collins", "Suzanne"], "The Hunger Games"),
            data.Book(["Collins", "Suzanne"], "Catching Fire"),
            data.Book(["Brown", "Dan"], "The Da Vinci Code"),
            data.Book(["Brown", "Dan"], "Angels & Demons"),
            data.Book(["Atwood", "Margaret"], "The Handmaid's Tale"),
            data.Book(["Orwell", "George"], "1984"),
            data.Book(["Orwell", "George"], "Animal Farm"),
            data.Book(["Shelley", "Mary"], "Frankenstein"),
        ]
        itv12 = "Suzanne Collins"
        final_r = hw1.books_by_author(itv12, test_catalog)
        expected = ["The Hunger Games","Catching Fire"]
        self.assertEqual(final_r, expected)





    # Part 7
    def test_circle_bound1(self):
        itv13 = data.Rectangle(data.Point(2, 8), data.Point(8, 2))
        expected = data.Circle(data.Point(5,5), 4.242640687119285)
        result_1 = hw1.circle_bound(itv13)
        self.assertEqual(result_1.center.x,expected.center.x)
        self.assertEqual(result_1.center.y,expected.center.y)
        self.assertAlmostEqual(result_1.radius, expected.radius, places = 3)

    def test_circle_bound2(self):
        itv14 = data.Rectangle(data.Point(-4, 6), data.Point(2, 0))
        result_2 = hw1.circle_bound(itv14)
        expected = data.Circle(data.Point(-1,3), 4.242640687119285)
        self.assertAlmostEqual(result_2.center.x,expected.center.x)
        self.assertAlmostEqual(result_2.center.y,expected.center.y)
        self.assertAlmostEqual(result_2.radius, expected.radius, places = 3)






    # Part 8
    def test_below_pay_rate1(self):
        itv15 = [
            data.Employee("A", 40),
            data.Employee("B", 50),
            data.Employee("C", 60),
            data.Employee("D", 70)
        ]
        expected = ["A", "B"]
        self.assertEqual(hw1.below_pay_average(itv15), expected)
    def test_below_pay_rate2(self):
        itv16 = [
                data.Employee("A", 10),
                data.Employee("B", 10),
                data.Employee("C", 30)
        ]
        expected = ["A", "B"]
        self.assertEqual(hw1.below_pay_average(itv16), expected)





if __name__ == '__main__':
    unittest.main()
