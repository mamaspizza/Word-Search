# Word-Search
Word Search Puzzle

A Python program that locates words in a 2 dimensional grid of letters and outputs the start and end coordinates for each of the words found. The program reads its input from a text file and writes its results to a text file. It only uses same number of rows and columns (X*X). Words can be search vertically or horizontally, forwards or backwards. Duplicate words are counted as one.
The program will be executed from command line with:  
python WordSearch.py puzzle1.pzl  
Where the parameter is the name of the input file. This will create an output file: puzzle1.out The output file contains one line for each word we are searching for in the following format:  
word (start coord x, start coord y) (end coord x, end coord y)  
Coordinates are relative to the top left hand corner of the grid, which is location (1, 1). 

Python codes:
  - WordSearch.py - main program
  - test.py - basic unit test for WordSearch
Example inputs:
  - animal.pzl
  - suits.pzl
  - lostDuck.pzl
  - numbers.pzl
  - large_puzzle.pzl
Inputs used for unit testing:
  - contains_lower_case.pzl
  - empty_file.pzl
  - first_row_length.pzl
  - puzzle_with_null.pzl
  - test_data.pzl
