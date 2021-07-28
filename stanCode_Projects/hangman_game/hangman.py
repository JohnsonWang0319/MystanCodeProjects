"""
File: hangman.py
Name: Johnson
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""

import random

# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    word = random_word()
    word_long = len(word)
    print('The word looks like: ' + '-' * word_long)
    print('You have ' + str(N_TURNS) + ' guesses left.')
    print(hangpic(N_TURNS))
    hangmen(word)


def hangmen(word):
    '''
    :param word: str, the random_word() will output a all caps letter word
    :return: str, print the situation of each stage
    '''
    global N_TURNS                                              # let the function can use the global variables
    correct = False                                             # when the correct = True the while loop will shut
    old_word = '-' * len(word)
    while correct == False and N_TURNS > 0:
        guess = input('Your guess: ')
        guess = guess.upper()

        if guess.isalpha() == True and len(guess) == 1:         # The partial_word and old_word will be used to
            initial_word = word_dash(guess, word)               # concatenate the partial word, which we need to show
            partial_word = ''                                   # in the console, such like: 'MA--U--A--'
            for i in range(len(initial_word)):
                if initial_word[i] != '-':
                    partial_word += initial_word[i]
                elif old_word[i] != '-':
                    partial_word += old_word[i]
                else:
                    partial_word += '-'

            if guess in word:                                   # If the letter is in the word, we have two situation,
                print('You are CORRECT!')                       # one is that the game is finished and the user win, and
                if '-' not in partial_word:                     # the other is that the user need to guess another
                    correct = True
                    print('You win!!')
                    print('The word was: ' + word)
                else:
                    print('The word looks like: ' + partial_word)
                    print('You have ' + str(N_TURNS) + ' guesses left.')
                    print(hangpic(N_TURNS))
                    old_word = partial_word
            else:                                               # Otherwise, we will lose one turns and need to guess
                N_TURNS -= 1                                    # another letter or we have already hung!
                print('There\'s no ' + guess + '\'s in the word.')
                if N_TURNS != 0:
                    print('The word looks like: ' + partial_word)
                    print('You have ' + str(N_TURNS) + ' guesses left.')
                    print(hangpic(N_TURNS))
                    old_word = partial_word
                else:
                    print(hangpic(N_TURNS))
                    print('You are completely hung :(')
                    print('The word was: ' + word)
        else:
            print('illegal format!')
    return


def word_dash(guess, word):
    '''
    :param guess: str, the user will input any letter
    :param word: str, the random_word() will output a all caps letter word
    :return: str, if the guess is 'A', then the word 'APPLE' will become 'A----'
    '''
    partial_word = ''
    for i in range(len(word)):
        if guess == word[i]:
            partial_word += word[i]
        else:
            partial_word += '-'
    return partial_word


def hangpic(n_turns):
    '''
    :param n_turns: int, the times that user left
    :return: image in the LIST
    '''
    image = ['''
                    +---***---+
                    |       |
                    |       O
                    |      \\|/
                    |       |
                    |      / \\
             ''',
             '''
                    +---***---+
                    |       |
                    |       O
                    |      \\|/
                    |       |
                    |        \\
             ''',
             '''
                    +---***---+
                    |       |
                    |       O
                    |      \\|/
                    |       |
                    |       
             ''',
             '''
                    +---***---+
                    |       |
                    |       O
                    |      \\|/
                    |       
                    |      
             ''',
             '''
                    +---***---+
                    |       |
                    |       O
                    |       |/
                    |        
                    |       
             ''',
             '''
                    +---***---+
                    |       |
                    |       O
                    |       | 
                    |        
                    |       
             ''',
             '''
                    +---***---+
                    |       |
                    |       O
                    |       
                    |        
                    |       
             ''',
             '''
                    +---***---+
                    |       |
                    |       Q
                    |       
                    |        
                    |       
             ''',
             ]

    if n_turns == 7:                # make every turns correspond to a image
        return image[0]
    if n_turns == 6:
        return image[1]
    if n_turns == 5:
        return image[2]
    if n_turns == 4:
        return image[3]
    if n_turns == 3:
        return image[4]
    if n_turns == 2:
        return image[5]
    if n_turns == 1:
        return image[6]
    if n_turns == 0:
        return image[7]

def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
