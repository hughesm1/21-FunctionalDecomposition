"""
Hangman.

Authors: PUT_YOUR_NAME_HERE and YOUR_PARTNERS_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Implement Hangman using your Iterative Enhancement Plan.

####### Do NOT attempt this assignment before class! #######

import random


def main():
    print("You can guess 4 incorrect times before you lose")
    count = 0
    anything = []
    x = rand_word()
    initial_dashes(x)
    # for k in range(len(x) + 4):
    while True:
        true_false, kval = guess(x)
        for h in range(len(kval)):
            anything = anything + [kval[h]]
        dashes(x, kval, anything)
        if count > len(x) + 4:
            print("congrats, you won!")
            break


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
    kk = []
    guess1 = input('What letter do you want to try?')
    for k in range(len(word)):
        if word[k] == guess1:
            kk = kk + [k]
    return True, kk
        # else:
        #     input("wrong guess, input something else")



def dashes(word, kval, anything):
    dash = []
    for k in range(len(word)):
        dash = dash + ['-']
    for u in range(len(anything)):
        index = anything[u]
        dash[index] = word[index]
    print(dash)


def initial_dashes(word):
    dash = []
    for k in range(len(word)):
        dash = dash + ['-']

# def find_indices(word, kval):
#     for k in range(len(word)):
#         if




main()