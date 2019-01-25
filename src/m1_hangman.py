"""
Hangman.

Authors: PUT_YOUR_NAME_HERE and YOUR_PARTNERS_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Implement Hangman using your Iterative Enhancement Plan.

####### Do NOT attempt this assignment before class! #######

import random


def main():
    print("You can guess as many times as you want")
    anything = []
    x = rand_word()
    initial_dashes(x)
    dashes(x, anything)
    while True:
        true_false, kval = guess(x)
        for h in range(len(kval)):
            anything = anything + [kval[h]]
        dash = dashes(x, anything)
        finished(dash, x)
        if finished(dash, x):
            print("congrats, you won!")
            break


def rand_word():
    with open('words.txt') as f:
        f.readline()
        string = f.read()
        words = string.split()
    r = random.randrange(0, len(words))
    word = words[r]
    return word


def guess(word):
    kk = []
    guess1 = input('What letter do you want to try?')
    for k in range(len(word)):
        if word[k] == guess1:
            kk = kk + [k]
    return True, kk


def dashes(word, anything):
    dash = []
    for k in range(len(word)):
        dash = dash + ['-']
    for u in range(len(anything)):
        index = anything[u]
        dash[index] = word[index]
    print(dash)
    return dash


def initial_dashes(word):
    dash = []
    for k in range(len(word)):
        dash = dash + ['-']


def finished(dash, word):
    for k in range(len(word)):
        if dash[k] == '-':
            return False
    return True


main()