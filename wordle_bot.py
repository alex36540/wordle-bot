"""
A program that solves wordle

Author: Alexander Lee
"""
import sys

# Constants
LETTER_DISTRIB_PATH = 'files/letter_distribution.txt'
DICT_PATH = 'files/5_letter_dict.txt'
FIRST_WORD = 'stare'

NO_MATCH = 0
YELLOW_LETTER = 1
GREEN_LETTER = 2


def usage():
    """
    Prints a usage message in case of bad arguments
    """
    print('Usage: python wordle_bot.py [word]')


def guess(word, guessed : set, yellow_letters : set, green_letters : dict):
    """
    Hardcoded solution not available to other methods. Returns a dictionary
    containing the status of whether each letter was correct, and also updates
    the letters guessed dictionary and yellow/green letter dictionaries.
    """
    for letter in word:
        guessed.add(letter)

    answer = 'shard'
    letter_set = set(answer)

    out_dict = {}
    
    # Test each condition on each letter
    for i in range(5):
        if word[i] == answer[i]:
            out_dict[i] = GREEN_LETTER

        elif word[i] in letter_set:
            out_dict[i] = YELLOW_LETTER

        else:
            out_dict[i] = NO_MATCH

    # Update the letter dictionaries based on the guess result dict
    #new_yellow_letters = set(yellow_letters)
    
    # if isinstance(green_letters, set):
    #new_green_letters = dict(green_letters)
    # else:
    #     new_green_letters = green_letters

    for i in range(5):
        if out_dict[i] == YELLOW_LETTER and word[i] not in green_letters:
            yellow_letters.add(word[i])

        elif out_dict[i] == GREEN_LETTER:
            green_letters.update({word[i]: i})

    return #new_yellow_letters, new_green_letters


def solve(word, word_dict, distrib):
    """
    Solves the puzzle based on a letter distribution and a dictionary
    of 5 letter words.
    """
    guessed = set()
    green_letters = dict()
    yellow_letters = set()

    guess(FIRST_WORD, guessed, yellow_letters, green_letters)
    print(guessed)
    print(yellow_letters)
    print(green_letters)
    print()


    guess('hsaoi', guessed, yellow_letters, green_letters)
    print(guessed)
    print(yellow_letters)
    print(green_letters)
    print()

    # TODO make words with repeated letters less likely





def main(word):
    """
    Runs an algorithm to solve Wordle
    """
    # Check input
    if len(word) != 5:
        print('Word must be 5 letters')
        return

    word_dict = set()

    # Get up 5 letter dictionary from file
    with open(DICT_PATH, 'r') as file:
        for line in file:
            word_dict.add(line.strip())

    # Set up letter distribution dict
    letter_distrib = {}
    
    with open(LETTER_DISTRIB_PATH, 'r') as file:
        for line in file:
            toks = line.split(' ')

            letter_distrib[toks[0]] = float(toks[1].strip())

    solve(word, word_dict, letter_distrib)




if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    
    else:
        usage()