import unittest
import os

from CoNLLContextManager import open_conll

class TestOpenConll(unittest.TestCase):
    def setUp(self):
        self.filename = "test.conll"
        with open(self.filename, "w") as f:
            f.write('"Ala"\t"Ala"\t"noun"\n"ma"\t"mieć"\t"verb"\n"kota"\t"kot"\t"noun"\n"."."\t"punct"')


    def tearDown(self):
        os.remove(self.filename)

    def test_iteration(self):
        with open_conll(self.filename) as infile:
            tokens = list(infile)
        self.assertEqual(tokens, [['Ala', 'Ala', 'noun'], ['ma', 'mieć', 'verb'], ['kota', 'kot', 'noun'], ['.', '.', 'punct']])

    def test_context_manager(self):
        with open_conll(self.filename) as infile:
            self.assertFalse(infile.file.closed)
        self.assertTrue(infile.file.closed)

    def test_non_existent_file(self):
        with self.assertRaises(FileNotFoundError):
            with open_conll("non_existent_file.conll") as infile:
                pass

if __name__ == "__main__":
    unittest.main()
