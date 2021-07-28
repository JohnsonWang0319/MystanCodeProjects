"""
File: boggle.py
Name: Johnson
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# Define the Boggle size
LEN_COL = 4
LEN_ROW = 4

# Global Variables
count = 0
boggle = []
now_word_lst = []


class TrieNode:
    """Node in the Trie Structure"""
    def __init__(self, char: str):
        # the character stored in the structure
        self.char = char
        # whether the end of a word or not
        self.end_of_word = False
        # indicate how many times a word is inserted
        self.counter = 0

        # a dictionary of child nodes
        # keys are characters, values are nodes
        self.children = {}


class Trie:
    """Trie Object"""

    def __init__(self):
        self.output_list = []
        # the trie root note does not store any character
        self.root = TrieNode('')

    def insert(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                # if a character is not found in trie, create a new node
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

        # mark the end of a word
        node.end_of_word = True
        node.counter += 1

    def find(self, node, prefix):
        """
        :param node: TriNode, the node to start with
        :param prefix: string, for tracing a word while traversing the trie structure
        """
        if node.end_of_word:
            self.output_list.append((prefix, node.counter))

        for child_value in node.children.keys():
            self.find(node.children[child_value], prefix + child_value)

    def query(self, x: str) -> list:
        """
        :param x: string, a input prefix
        :return: list, retrieve all words stored in the trie with input prefix
        """
        node = self.root
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                return []
        self.find(node, x)
        return sorted(self.output_list, key=lambda z: z[1], reverse=True)

    def search(self, word: str):
        """
        :param word: string, a complete word
        :return: bool, whether this word in the trie structure or not
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end_of_word


def main():
    """
    Use the Trie structure to find the matched word between dictionary and boggle matrix
    """
    print(f'# of Column = {LEN_COL}.')
    print(f'# of Row = {LEN_ROW}.')
    start = time.time()
    t = Trie()
    build_boggle()

    for row in range(LEN_ROW):
        for column in range(LEN_COL):
            dict_lst = read_dictionary()
            for i in range(len(dict_lst)):
                word = dict_lst[i]
                if len(word) >= 4 and word[0] == boggle[row][column]:
                    t.insert(word)
            current = t.root
            dfs(row, column, [], current.children, '', row, column)

    end = time.time()
    print(f'There are {count} words in total.')
    print('----------------------------------')
    print(f'The speed of your boggle algorithm: {end - start} seconds.')


def dfs(row, column, visited, trie_children, now_word, original_row, original_column):
    """
    :param row: int, the row (neighbors) that we need to update everytime when execute this function
    :param column: int, the column (neighbors) that we need to update everytime when execute this function
    :param visited: list, [(row, column)], the index that we have already visited while traverse the boggle
    :param trie_children: TrieNode, the trie structure that we need to compare during traverse the boggle
    :param now_word: str, update during the recursion, and if it is the end_of_word, we found answer
    :param original_row: the row that we traverse in the first round, using this to pruning the trie structure
    :param original_column: the column that we traverse in the first round, using this to pruning the trie structure
    :return:
    """
    global count
    t = Trie()
    dict_lst = read_dictionary()

    if (row, column) in visited:
        return
    letter = boggle[row][column]
    original_letter = boggle[original_row][original_column]
    visited.append((row, column))

    # when now_word length >= 3, start to generate trie structure of the dictionary
    if len(now_word) >= 3:
        for i in range(len(dict_lst)):
            word = dict_lst[i]
            if len(word) >= 4 and word[0] == original_letter:
                t.insert(word)

    # if the letter is in the trie_children, keep finding the next children.
    if letter in trie_children and len(now_word) <= LEN_ROW + 2:
        now_word += letter
        current = trie_children[letter]

        # Because it would be possible that there is the same word in different combination of boggle matrix
        # Use a if to check whether there is the same matched word in the now_word_lst
        if len(now_word) >= 4 and now_word not in now_word_lst:

            # Use t.search to determine whether now_word is a complete word in trie structure or not
            if t.search(now_word):
                now_word_lst.append(now_word)
                print(f'Found \"{now_word}\"')
                count += 1

        # Use recursive to achieve depth-first traversal (each neighbor)
        neighbors = get_neighbors(row, column)
        for n in neighbors:
            dfs(n[0], n[1], visited[:], current.children, now_word, original_row, original_column)


def build_boggle():
    """
    Ask user to input the boggle matrix, user can determine the matrix size by controlling the global variable LEN_ROW
    and LEN_COL.
    :return: list, [[X, X, X, X],[X, X, X, X],[X, X, X, X],[X, X, X, X]]
    """
    count_input = 0
    while count_input != LEN_ROW:
        row = input(f'{count_input + 1} row of letters: ').split(' ')
        if len(row) != LEN_COL:
            print('Illegal input.')
            exit()
        else:
            boggle.append(row)
            count_input += 1
    return boggle


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    # dict_list = ['apple', 'banana', 'cat', 'dog' ......]
    dict_list = []
    with open(FILE, 'r') as f:
        for line in f:
            line = line.strip('\n')
            dict_list.extend(line.split())
    return dict_list


def get_neighbors(row, column):
    """
    :param row: int, the row index
    :param column: int, the column index
    :return: list, all the neighbors of a specific index, [(),(),(),(),(),(),(),()]
    """
    # Return the neighbors fo a given coordinates
    neighbors = []
    neighbors_index = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for neighbor in neighbors_index:
        new_row = row + neighbor[0]
        new_column = column + neighbor[1]
        if new_row >= LEN_ROW or new_column >= LEN_COL or new_row < 0 or new_column < 0:
            continue
        neighbors.append((new_row, new_column))
    return neighbors


if __name__ == '__main__':
    main()
