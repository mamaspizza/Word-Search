""" Word Search Puzzle
    This program locates words in a 2 dimensional grid of letters and outputs the start
    and end coordinates for each of the words found.
    Command arguments: WordSearch.py [input file] [output file]
        input file is required while output file is optional
"""
import sys
import os


def search(argv):
    """ Call here the required functions to find the words in puzzle
        'argv': Command arguments
    """
    # 1. Process the input to array of characters
    # 2. Use the array in our search algorithm
    (array_chars, words) = process_input(argv)
    words_in_pzl = find_words(array_chars, words)

    # 3. Write the result in output file
    output_file = (argv[1]).split('.')[0]
    output_file = output_file + '.out'
    if len(argv) < 2:
        output_file = argv[2]
    with open(output_file, 'w') as f:
        for found_word, coords in words_in_pzl.items():
            w = ''
            if len(coords) != 0:
                # Print the first coordinate
                # since instruction says print only one
                str_coords = str(coords[0])
                w = '{word} {coords}\n'.format(word=found_word, coords=str_coords)
            else:
                w = '{} not found\n'.format(found_word)
            f.write(w)

def process_input(argv):
    """ This will put the characters into array of characters.
        'argv': Command arguments
    """
    if len(argv) < 2:
        raise Exception("Command Arguments should include input file puzzle.")
    filepath = argv[1]
    if not os.path.exists(filepath):
        raise Exception("Input file does not exist.")

    array_chars = []
    words = []
    max_rows = 0
    # read flag values
    # 0 - read input
    # 1 - read output
    # greater 1 - stop
    read_flag = 0
    with open(filepath, 'r') as f:

        lines = f.readlines()
        for line in lines:
            # We will always base the maximum row length
            # to the first row of the puzzle
            if max_rows == 0:
                max_rows = len(line.strip())
            if len(line.strip()) == 0:
                read_flag += 1
                continue

            if read_flag == 0:
                data = ''
                if len(line) < max_rows:
                    # add additional null data to complete the one dimension puzzle
                    data = line.ljust(max_rows).strip().upper()
                else:
                    data = line[0:max_rows].strip().upper()
                array_chars.append(data)
            elif read_flag == 1:
                words.append(line.strip().upper())
    return array_chars, words

def find_words(array_chars, words):
    """ This functions will construct candidates and look if it exist
        in the words. This will return list of words with coordinates
        where they are located in the puzzle.
        'array_chars': input puzzle which contains array of characters.
        'words': array of words for search.
    """

    words_in_pzl = {}
    for word in words:
        words_in_pzl[word] = []

    if len(words) == 0:
        return words_in_pzl

    # Process each characters in the array
    for rindex, row in enumerate(array_chars):
        for cindex, val in enumerate(row):
            # Up direction to construct candidates
            temp = cindex
            candidate = val
            while True:
                temp -= 1
                if temp < 0:
                    break
                candidate += array_chars[rindex][temp]
                if candidate in words:
                    coord = ((cindex + 1, rindex + 1)
                             , (temp + 1, rindex + 1))
                    words_in_pzl[candidate].append(coord)

            # Down direction to construct candidates
            temp = cindex
            candidate = val
            row_length = len(row)
            while True:
                temp += 1
                if temp >= row_length:
                    break
                candidate += array_chars[rindex][temp]
                if candidate in words:
                    coord = ((cindex + 1, rindex + 1)
                             , (temp + 1, rindex + 1))
                    words_in_pzl[candidate].append(coord)

            # Left direction to construct candidates
            temp = rindex
            candidate = val
            while True:
                # stop if reaches last row id
                if temp == 0:
                    break
                temp -= 1
                candidate += array_chars[temp][cindex]
                if candidate in words:
                    coord = ((cindex + 1, rindex + 1)
                             , (cindex + 1, temp + 1))
                    words_in_pzl[candidate].append(coord)

            # Right direction to construct candidates
            temp = rindex
            candidate = val
            while True:
                # stop if reaches last row id
                temp += 1
                if temp >= len(array_chars):
                    break

                candidate += array_chars[temp][cindex]
                if candidate in words:
                    coord = ((cindex + 1, rindex + 1)
                             , (cindex + 1, temp + 1))
                    words_in_pzl[candidate].append(coord)

    return words_in_pzl


if __name__ == "__main__":    
    search(sys.argv)
