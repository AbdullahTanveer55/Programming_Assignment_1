import data
import unittest
import hw1


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test01_vowel_count(self):
        string = hw1.vowel_count('I am Abdullah a')
        self.assertEqual(string, 6)


    # Part 2
    def test02_short_lists(self):
        intgr = hw1.short_lists([[8, 5, 3, 2], [1, 2], [6, 8], [9, 7, 5, 3]])
        self.assertEqual(intgr, [[1, 2], [6, 8]])


    # Part 3
    def test03_ascending_pair(self):
        intgr = hw1.ascending_pair([[8, 6], [8, 5, 3, 2], [2, 1], [9, 7, 5, 3]])
        self.assertEqual(intgr, [[6, 8], [8, 5, 3, 2], [1, 2], [9, 7, 5, 3]])


    # Part 4
    def test04_add_prices(self):
        price_one = hw1.add_prices(20.53, 19.99)
        price_two = hw1.add_prices(20.53, 19.99)
        self.assertEqual(price_one, price_two, 40.52)


    # Part 5
    def test05_rectangle_area(self):
        rectangle = hw1.rectangle_area(9)
        self.assertEqual(rectangle, 9)


     # Part 6
    def test_books_by_author1(self):
        book1 = data.Book(['Neil Gaiman', "Terry Pratchett"], 'Good Omens')
        book2 = data.Book(["Robert Kiyosaki"], "Rich dad poor dad")
        book3 = data.Book(["Robert Kiyosaki"], "Another book")
        input1 = ["Robert Kiyosaki"]
        input2 = [book1, book2, book3]
        result = hw1.books_by_author(input1, input2)
        expected = data.Book(["Robert Kiyosaki"], "Rich dad poor dad"), data. Book(["Robert Kiyosaki"], "Another book")
        self.assertEqual(expected, result)

   # def test_books_by_author2(self):
      #  input = [data.Book(["Rick Riordan"], "Percy Jackson: The Lightning Thief"), data.Book(["Rick Riordan"],
               #  "Percy Jackson: The sea of Monsters"), data.Book(["Rick Riordan"], "The Lost Hero"), data.Book(["Robert Kiyosaki"], "Rich dad poor dad")]
       # expected = [data.Book(["Rick Riordan"], "Percy Jackson: The Lightning Thief"), data.Book(["Rick Riordan"],
          #  "Percy Jackson: The Sea of Monsters"), data.Book(["RicK Riordan"], "The Lost Hero")]
     #   result = hw1.books_by_author(["Rick Riordan"], input)
      #  self.assertEqual(expected, result)

        # Part 7
    def test07_circle_bound(self):
        result = data.Circle(data.Point(3.0, 3.0), 5.0)
        rec = data.Rectangle(data.Point(0, -1), data.Point(6, 7))
        self.assertEqual(result, hw1.circle_bound(rec))

    def test_07_circle_bound2(self):
        result = data.Circle(data.Point(3.5, 3.0), 2.5)
        rec = data.Rectangle(data.Point(2, 1), data.Point(5, 5))
        self.assertEqual(result, hw1.circle_bound(rec))


    # Part 8
    def test08_below_pay_average(self):
        answer = ['Abdullah', 'Jack', 'Adam']
        employee_list = [data.Employee("Abdullah", 16), data.Employee("Jack", 18), data.Employee("Tristian", 22),
                     data.Employee("Adam", 17), data.Employee("John", 25), data.Employee("Adam", 21)]

        self.assertEqual(answer, hw1.below_pay_average(employee_list))
























if __name__ == '__main__':
    unittest.main()
