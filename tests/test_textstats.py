import unittest
from textstats import average_word_length, word_count


class TextStatsTests(unittest.TestCase):
    def test_word_count_simple(self):
        self.assertEqual(word_count("hello world"), 2)

    def test_average_word_length(self):
        self.assertEqual(average_word_length("ab abcd"), 3.0)


if __name__ == "__main__":
    unittest.main()
