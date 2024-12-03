import pytest
from src.homework.text_ops import count_words, find_longest_word, format_sentences
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


class TestTextOps(CustomTestCase):
    def setUp(self):
        self.sample_text = "Python is an amazing programming language! It is easy to learn."

    def test_count_words(self):
        if not is_implemented(count_words, self.sample_text):
            self.skipTest("Not yet implemented")
        print("\nTesting count_words:")
        result = count_words(self.sample_text)
        self.assertEqual(result['python'], 1)
        self.assertEqual(result['is'], 2)
        #self.assertEqual(len(result), 7)
        self.assertEqual(len(result), 10)
        self.assertEqual(count_words(""), {})

    def test_find_longest_word(self):
        if not is_implemented(find_longest_word, self.sample_text):
            self.skipTest("Not yet implemented")
        print("\nTesting find_longest_word:")
        self.assertEqual(find_longest_word(self.sample_text), "programming")
        self.assertEqual(find_longest_word(""), "")

    def test_format_sentences(self):
        if not is_implemented(format_sentences, self.sample_text):
            self.skipTest("Not yet implemented")
        print("\nTesting format_sentences:")
        result = format_sentences(self.sample_text)
        self.assertEqual(len(result), 2)
        self.assertTrue(result[0].startswith("Python"))
        self.assertTrue(result[1].startswith("It"))


if __name__ == '__main__':
    unittest.main(verbosity=2)
