"""
Hangman.

Authors: PUT_YOUR_NAME_HERE and YOUR_PARTNERS_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Implement Hangman using your Iterative Enhancement Plan.

####### Do NOT attempt this assignment before class! #######

import random


def main():
    anything = []
    x = rand_word()
    initial_dashes(x)
    for k in range(3):
        true_false, kval = guess(x)
        anything = anything + [kval]
        dashes(x, kval, anything)


def rand_word():
    with open('words.txt') as f:
        f.readline()
        string = f.read()
        words = string.split()
    r = random.randrange(0, len(words))
    word = words[r]
    print(word)
    return word

# def word_length():
#     variable = input('Minimum length of word')
#     if variable


def guess(word):
    guess1 = input('What letter do you want to try?')
    for k in range(len(word)):
        if word[k] == guess1:
            print(word[k])
            return True, k



def dashes(word, kval, anything):
    dash = []
    for k in range(len(word)):
        dash = dash + ['-']
    for u in range(len(anything) + 1):
        dash[kval] = word[kval]
    print(kval)
    print(anything[0])
    print(word[0])
    print(dash)


def initial_dashes(word):
    dash = []
    for k in range(len(word)):
        dash = dash + ['-']






main()