# code must be checked in to github

# there needs to be a UI to enter baseboard numbers
# and a way to see the solution

# 9x9 standard board size 

# three methods required : setboard, solveboard, showsolution

#input pandas dataframe

#-----------------------------------------#

#imports
import pandas as pd
import numpy as np
import random

#global variables
size = 3

def create_test_board():
    testboard = np.full([size,size], fill_value = -1, dtype=int)
    return testboard

def setboard():
    pass

def fill_row(board,rowindex):
    if rowindex == 0: #first row
        options = [i+1 for i in range(size)]
        colindex = 0
        while True:
            if len(options) == 1:
                board[0][size-1] = options[0]
                break
            guess_index = random.randint(0,len(options)-1)
            guess = options[guess_index]
            board[0][colindex] = guess
            #increment colindex
            colindex += 1
            #delete the guess from options
            del options[guess_index]
        return 0
    #below here is for cases that arent the first row
    prev_guessed = []
    options = []
    for i in range(size):
        #if index is 0, then only check above
        if i == 0:
            above = board[rowindex-1,i]
            #create options list
            for j in range(size):
                if (j+1) == above:
                    continue
                options.append(j+1)
            #create first guess
            guess_index = random.randint(0,len(options)-1)
            guess = options[guess_index]
            #set board with guess
            board[rowindex][i] = guess
            #remove guess from list and append to prev_guessed
            del options[guess_index]
            prev_guessed.append(guess)
            print(f'guess {i} = {guess}')
            continue
        #not the first guess so we need to check above and to the left
        options = []
        above = board[rowindex-1,i]
        left = board[rowindex, i-1]
        #fill options list
        test_set = set(prev_guessed)
        for j in range(size):
            if ((j+1) == above) or ((j+1) == left) or ((j+1) in test_set):
                continue
            options.append(j+1)
        if len(options) == 0:
            print('invalid solution')
            print('prev:',prev_guessed)
            return -1
        #make guess for left and above cells
        elif len(options) == 1:
            guess = options[0]
            prev_guessed.append(guess)
            board[rowindex, i] = guess
            print(f'guess {i} = {guess}')
        else: # there are two options
            guess_index = random.randint(0,len(options)-1)
            guess = options[guess_index]
            board[rowindex, i] = guess
            print(f'guess {i} = {guess}')
    return 0
    #test
    print(options)

        


def solve(board):
    #fill first row 
    fill_row(board = board,rowindex = 0)
    #fill second row
    while True:
       test = fill_row(board = board, rowindex = 1)
       if test == 0:
        break
    #fill third row?
    fill_row(board = board, rowindex = 2)
    #test block

    return board 

def main():
    board = create_test_board()

    board = solve(board)
    print(board)

main()