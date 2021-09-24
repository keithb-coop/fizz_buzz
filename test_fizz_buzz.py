import unittest

from fizz_buzz import fizz_buzz


class TestFizzBuzz(unittest.TestCase):
    def test_one_returns_one(self):
        result = fizz_buzz(1)
        self.assertEqual(result, 1)

    def test_three_returns_fizz(self):
        result = fizz_buzz(3)
        self.assertEqual(result, 'Fizz')

    def test_five_returns_buzz(self):
        result = fizz_buzz(5)
        self.assertEqual(result, 'Buzz')
    
    def test_seven_returns_baz(self):
        result = fizz_buzz(7)
        self.assertEqual(result, 'Baz')

    def test_multiple_of_three_returns_fizz(self):
        result = fizz_buzz(6)
        self.assertEqual(result, 'Fizz')

    def test_multiple_of_five_returns_buzz(self):
        result = fizz_buzz(10)
        self.assertEqual(result, 'Buzz')
    
    def test_multiple_of_seven_returns_baz(self):
        result = fizz_buzz(14)
        self.assertEqual(result, 'Baz')


if __name__ == "__main__":
    unittest.main()
