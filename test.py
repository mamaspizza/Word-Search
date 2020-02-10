""" This is a basic test for WordSearch program """
import unittest
import WordSearch


class TestWordSearch(unittest.TestCase):

    def test_valid_file_input(self):
        """ Test a valid input file. """        
        input_file = 'animal.pzl'
        argv = ['', input_file]

        (chars_array, words) = WordSearch.process_input(argv)

        expected_array = ['CIRN', 'ADOG', 'TCIS', 'KCOW']
        self.assertListEqual(chars_array, expected_array)
        expected_words = ['CAT', 'DOG', 'COW']
        self.assertListEqual(words, expected_words)

    def test_puzzle_has_null_input(self):
        """ Test puzzle has null string input. """
        input_file = 'puzzle_with_null.pzl'
        argv = ['', input_file]
        
        (chars_array, words) = WordSearch.process_input(argv)

        expected_array = ['CIRN', 'AD G', 'TCIS', 'KCOW']
        self.assertListEqual(chars_array, expected_array)

    def test_puzzle_first_row_length(self):
        """ Test the length or first row should follow length
            of other next rows.
        """
        input_file = 'first_row_length.pzl'
        argv = ['', input_file]

        (chars_array, words) = WordSearch.process_input(argv)

        expected_array = ['CIR', 'ADO', 'TCI', 'KCO']
        self.assertListEqual(chars_array, expected_array)

    def test_puzzle_char_lower_case(self):
        """ Test the length or first row should follow length
            of other next rows.
        """
        input_file = 'contains_lower_case.pzl'
        argv = ['', input_file]

        (chars_array, words) = WordSearch.process_input(argv)

        expected_array = ['CIRN', 'ADOG', 'TCIS', 'KCOW']
        self.assertListEqual(chars_array, expected_array)
        expected_words = ['CAT', 'DOG', 'COW']
        self.assertListEqual(words, expected_words)

    def test_empty_input_file(self):
        """ Test the file input empty.
        """
        input_file = 'empty_file.pzl'
        argv = ['', input_file]

        (chars_array, words) = WordSearch.process_input(argv)
        
        self.assertEqual(chars_array, [])
        self.assertEqual(words, [])

        word_output = WordSearch.find_words(chars_array, words)
        self.assertEqual(word_output, {})

    def test_words_going_up(self):
        """ Different cases where words are searched upwards. """
        input_file = 'test_data.pzl'
        argv = ['', input_file]

        (chars_array, words) = WordSearch.process_input(argv)

        # Left top
        key = 'LEMON'
        words.append(key)
        word_output = WordSearch.find_words(chars_array, words)
        expected_coord = [((11, 20), (11, 16))]
        self.assertListEqual(word_output[key], expected_coord)

        # Bottom rightmost
        words = []
        key = 'ORANGE'
        words.append(key)
        word_output = WordSearch.find_words(chars_array, words)
        expected_coord = [((20, 20), (20, 15))]
        self.assertListEqual(word_output[key], expected_coord)

        # Middle
        words = []
        key = 'APPLE'
        words.append(key)
        word_output = WordSearch.find_words(chars_array, words)
        expected_coord = [((10, 10), (10, 6))]
        self.assertListEqual(word_output[key], expected_coord)

    def test_words_going_left(self):
        """ Different cases where words are searched going to left. """
        input_file = 'test_data.pzl'
        argv = ['', input_file] 
        (chars_array, words) = WordSearch.process_input(argv)

        # Right top
        key = 'CHERRY'
        words.append(key)
        word_output = WordSearch.find_words(chars_array, words)
        expected_coord = [((20, 1), (15, 1))]
        self.assertListEqual(word_output[key], expected_coord)

        # Bottom Left
        words = []
        key = 'BANANA'
        words.append(key)
        word_output = WordSearch.find_words(chars_array, words)
        expected_coord = [((8, 18), (3, 18))]
        self.assertListEqual(word_output[key], expected_coord)

        # Middle
        words = []
        key = 'GUAVA'
        words.append(key)
        word_output = WordSearch.find_words(chars_array, words)
        expected_coord = [((14, 10), (10, 10))]
        self.assertListEqual(word_output[key], expected_coord)

    def test_found_word_in_different_pos(self):
        """ Test a word that is in different position in the puzzle """
        input_file = 'test_data.pzl'
        argv = ['', input_file]
        (chars_array, words) = WordSearch.process_input(argv)

        # Right top
        key = 'PEACH'
        words.append(key)
        word_output = WordSearch.find_words(chars_array, words)
        self.assertEqual(len(word_output[key]), 8)

        expected_coords = [((2, 2), (6, 2))
                         , ((20, 6), (16, 6))
                         , ((20, 6), (20, 2))
                         , ((9, 10), (5, 10))
                         , ((9, 10), (9, 14))
                         , ((19, 18), (19, 14))
                         , ((2, 2), (2, 6))
                         , ((1, 20), (5, 20))]
        for exp_ccord in expected_coords:
            self.assertTrue(exp_ccord in word_output[key])


if __name__ == "__main__":
    unittest.main()
