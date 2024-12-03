import pytest
from src.homework.search import binary_search_iterative, binary_search_recursive
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


class TestBinarySearch(CustomTestCase):
    def setUp(self):
        self.sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]

    def test_binary_search_iterative(self):
        if not is_implemented(binary_search_iterative, self.sorted_list, 7):
            self.skipTest("Not yet implemented")
        print("\nTesting binary_search_iterative:")
        self.assertEqual(binary_search_iterative(self.sorted_list, 7), 3)
        self.assertEqual(binary_search_iterative(self.sorted_list, 15), 7)
        self.assertEqual(binary_search_iterative(self.sorted_list, 10), -1)
        self.assertEqual(binary_search_iterative([], 5), -1)

    def test_binary_search_recursive(self):
        if not is_implemented(binary_search_recursive, self.sorted_list, 7, 0, 7):
            self.skipTest("Not yet implemented")
        print("\nTesting binary_search_recursive:")
        self.assertEqual(binary_search_recursive(self.sorted_list, 7, 0, 7), 3)
        self.assertEqual(binary_search_recursive(self.sorted_list, 15, 0, 7), 7)
        self.assertEqual(binary_search_recursive(self.sorted_list, 10, 0, 7), -1)
        self.assertEqual(binary_search_recursive([], 5, 0, -1), -1)


if __name__ == '__main__':
    unittest.main(verbosity=2)