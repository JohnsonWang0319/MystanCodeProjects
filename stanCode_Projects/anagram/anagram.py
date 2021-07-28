"""
File: anagram.py
Name: Johnson
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time  # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'  # Controls when to stop the loop

# Global Variables
dict_lst = []
anagrams_lst = []
same = []


def main():
    """
    Finding the anagram in the dictionary.
    When user type a word, this program will generate the anagram and calculate the searching time.
    """
    # Set the counter to count the number of anagram.
    count = 0

    # Begin the calculate the searching time.
    start = time.time()

    read_dictionary()
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')

    while True:
        anagram = input('Find anagrams for: ')

        # Exit condition
        if anagram == '-1':
            print('Goodbye!')
            break

        else:
            # Using the recursive method to generate anagram and add into anagrams_lst
            find_anagrams(anagram)

            # To check the anagrams_lst element in dict_lst or not
            for i in range(len(anagrams_lst)):
                anagram = anagrams_lst[i]
                for j in range(len(anagram)):
                    char = anagram[:j-2]
                    if has_prefix(char):

                        # Check anagram not in the same_lst to avoid adding same anagram
                        if anagram in dict_lst and anagram not in same:
                            print('Searching...')
                            print(f'Found: {anagram}!')

                            # Append the word that occur in both dict_lst and anagrams_lst.
                            same.append(anagram)
                            count += 1

            print(f'{count} anagrams: {same}')
            end = time.time()
            # End of the calculate of searching time.

            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary():
    with open(FILE, 'r') as f:
        for line in f:
            line = line.strip('\n')
            dict_lst.extend(line.split())


def find_anagrams(s):
    """
    :param s: (int) The word that user type.
    :return: Using another function to append list element into anagrams_lst.
    """
    find_anagrams_helper(list(s), [], len(list(s)))


def find_anagrams_helper(word_lst, current_lst, ans_len):
    if len(current_lst) == ans_len:
        anagrams_lst.append(''.join(current_lst))
    else:
        for i in range(len(word_lst)):
            char = word_lst[i]
            if current_lst.count(char) >= word_lst.count(char):
                pass
            else:
                # Choose
                current_lst.append(char)
                # Explore
                find_anagrams_helper(word_lst, current_lst, ans_len)
                # Un-choose
                current_lst.pop()


def has_prefix(sub_s):
    """
    :param sub_s: (str) The beginning character of the word.
    :return: If there are words in dict_lst start with sub_s, return True. Otherwise, return True.
    """
    for i in range(len(dict_lst)):
        word = str(dict_lst[i])
        if word.startswith(sub_s):
            return True
        else:
            return False


if __name__ == '__main__':
    main()
