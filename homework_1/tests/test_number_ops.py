import pytest
from src.homework.number_ops import fibonacci_recursive, sum_of_digits_recursive, is_palindrome_number
import unittest


class CustomTestCase(unittest.TestCase):
    def assertEqual(self, first, second, msg=None):
        try:
            super().assertEqual(first, second, msg)
            print("\033[32mExcellent! Function implemented correctly! Keep going! 🎉\033[0m\n")
        except AssertionError:
            print("\033[31mOops! Something went wrong... but don't panic! Everyone makes mistakes. "
                  "Try again, fix the code, and you'll be back on track! 🚀\033[0m")
            raise


def is_implemented(func, *args):
    try:
        result = func(*args)
        return result is not None
    except Exception:
        return False


class TestNumberOps(CustomTestCase):
    def test_fibonacci_recursive(self):
        if not is_implemented(fibonacci_recursive, 5):
            self.skipTest("Not yet implemented")
        print("\nTesting fibonacci_recursive:")
        self.assertEqual(fibonacci_recursive(0), 0)
        self.assertEqual(fibonacci_recursive(1), 1)
        self.assertEqual(fibonacci_recursive(8), 21)
        with self.assertRaises(ValueError):
            fibonacci_recursive(-1)

    def test_sum_of_digits_recursive(self):
        if not is_implemented(sum_of_digits_recursive, 123):
            self.skipTest("Not yet implemented")
        print("\nTesting sum_of_digits_recursive:")
        self.assertEqual(sum_of_digits_recursive(12345), 15)
        self.assertEqual(sum_of_digits_recursive(0), 0)
        self.assertEqual(sum_of_digits_recursive(-123), 6)

    def test_is_palindrome_number(self):
        if not is_implemented(is_palindrome_number, 12321):
            self.skipTest("Not yet implemented")
        print("\nTesting is_palindrome_number:")
        self.assertTrue(is_palindrome_number(12321))
        self.assertFalse(is_palindrome_number(12345))
        self.assertTrue(is_palindrome_number(0))
        self.assertFalse(is_palindrome_number(-12321))


if __name__ == '__main__':
    unittest.main(verbosity=2)
