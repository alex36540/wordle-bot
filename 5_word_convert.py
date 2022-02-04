import sys

OUTPUT_PATH = 'files/5_letter_dict.txt'

def main(dict_path):
    """
    Takes a file containing all words in the dictionary
    and outputs a new file containing all words in the original
    dictionary with 5 letters.
    """
    five_word_dict = []
    
    with open(dict_path, 'r') as dictionary:
        five_word_dict = []
        
        for line in dictionary:
            word = line.strip()

            if len(word) == 5:
                five_word_dict.append(word)

    with open(OUTPUT_PATH, 'w') as out:
        for word in five_word_dict:
            out.write(word + '\n')


if __name__ == '__main__':
    main(sys.argv[1])