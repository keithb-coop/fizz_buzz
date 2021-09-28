import unittest

from fizz_buzz import fizz_buzz


class TestFizzBuzz(unittest.TestCase):
    def test_one_returns_one(self):
        result = fizz_buzz(1)
        self.assertEqual("1", result)

    def test_three_returns_fizz(self):
        result = fizz_buzz(3)
        self.assertEqual('Fizz', result)

    def test_five_returns_buzz(self):
        result = fizz_buzz(5)
        self.assertEqual('Buzz', result)
    
    def test_seven_returns_baz(self):
        result = fizz_buzz(7)
        self.assertEqual('Baz', result)

    def test_multiple_of_three_returns_fizz(self):
        result = fizz_buzz(6)
        self.assertEqual('Fizz', result)

    def test_multiple_of_five_returns_buzz(self):
        result = fizz_buzz(10)
        self.assertEqual('Buzz', result)
    
    def test_multiple_of_seven_returns_baz(self):
        result = fizz_buzz(14)
        self.assertEqual('Baz', result)


if __name__ == "__main__":
    unittest.main()
