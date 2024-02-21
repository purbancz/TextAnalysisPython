import unittest
import os

from NgramCounter import generate_tokens, generate_n_grams, count_tokens, get_top_n_with_ties

class TestNgramCounter(unittest.TestCase):
    def setUp(self):
        self.filename = "test.txt"
        with open(self.filename, "w") as f:
            f.write("This is a test file. This file is used for testing.")

    def tearDown(self):
        os.remove(self.filename)

    def test_generate_tokens(self):
        tokens = list(generate_tokens(self.filename))
        self.assertEqual(tokens, ["This", "is", "a", "test", "file.", "This", "file", "is", "used", "for", "testing."])

    def test_generate_n_grams(self):
        n_grams = list(generate_n_grams(self.filename, 2))
        self.assertEqual(n_grams, ["This is", "is a", "a test", "test file.", "file. This", "This file", "file is", "is used", "used for", "for testing."])

    def test_count_tokens(self):
        token_counts = count_tokens(generate_tokens(self.filename))
        self.assertEqual(token_counts, {"This": 2, "is": 2, "a": 1, "test": 1, "file.": 1, "file": 1, "used": 1, "for": 1, "testing.": 1})

    def test_get_top_n_with_ties(self):
        token_counts = count_tokens(generate_tokens(self.filename))
        top_tokens = get_top_n_with_ties(token_counts, 1)
        self.assertEqual(top_tokens, [("This", 2), ("is", 2)])

if __name__ == "__main__":
    unittest.main()
