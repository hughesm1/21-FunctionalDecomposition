"""
Hangman.

Authors: Marcus Hughes-Oliver and Nihaar Reddy.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# DONE: 2. Implement Hangman using your Iterative Enhancement Plan.

####### Do NOT attempt this assignment before class! #######

import random


def main():
    mhmm = True
    while mhmm:
        min_length = int(input('what minimum length of a word do you want?'))
        incorrect = int(input('how many incorrect guesses do you want to have before you lose?'))
        print("You have ", incorrect, " incorrect guesses before you lose")
        yep = ''
        anything = []
        x = check_length(min_length)
        str(dashes(x, anything))
        yep = loopy_loop(x, anything, yep, mhmm, incorrect)
        mhmm = play_again(yep)
    print("thanks for playing")


def loopy_loop(x, anything, yep, mhmm, incorrect):
    count = 0
    while mhmm:
        true_false, kval, count = guess(x, count)
        for h in range(len(kval)):
            anything = anything + [kval[h]]
        dash = dashes(x, anything)
        make_string(dash)
        print('you have ', count, ' incorrect guesses, you have, ', incorrect-count, ' guesses left before you lose')
        if finished(dash, x):
            yep = input('congrats you won, do you want to play again(y,n)')
            return yep
        if count == incorrect:
            print('you lose, the word you couldnt guess was ', x)
            yep = input('do you want to play again(y,n)')
            return yep


def rand_word():
    with open('words.txt') as f:
        f.readline()
        string = f.read()
        words = string.split()
    r = random.randrange(0, len(words))
    word = words[r]
    return word


def check_length(min_length):
    while True:
        word = rand_word()
        if len(word) >= min_length:
            return word


def guess(word, count):
    kk = []
    lenk = 0
    guess1 = input('What letter do you want to try?')
    for k in range(len(word)):
        if word[k] == guess1:
            kk = kk + [k]
    if len(kk) == lenk:
        count = count + 1
    lenk = len(kk)

    return True, kk, count


def dashes(word, anything):
    dash = []
    for k in range(len(word)):
        dash = dash + ['-']
    for u in range(len(anything)):
        index = anything[u]
        dash[index] = word[index]
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


def play_again(yep):
    if "y" == yep:
        return True
    elif "n" == yep:
        return False
    else:
        print('you didnt put the right thing in, do it again')
        while True:
            wow = input('put either y or n')
            if wow == 'y':
                return True
            elif wow == 'n':
                return False


def make_string(dash):
    stringy = ''
    for k in range(len(dash)):
        stringy = stringy + dash[k] + ' '
    print(stringy)


main()