import pandas as pd
import numpy as np

puzzles_df = pd.read_csv('puzzles/sudoku-3m.csv')

def setup_puzzle(puzzle_id):
    global puzzles_df
    puzzlestr = puzzles_df.loc[puzzle_id-1].puzzle

    grid = np.zeros(shape = (9,9), dtype = int)
    for index, char in enumerate(puzzlestr):
        row = int(index/9)
        col = index % 9
        if char == '.':
            grid[row][col] = 0
        else:
            grid[row][col] = int(char)
    return grid 


def validator(xpos, ypos, n, puzzle):
    #check if row contains duplicate value
    for i in puzzle[ypos]:
        if i == n:
            return False
    #check if col containts duplicate value
    for row in puzzle:
        if row[xpos] == n:
            return False
    #check if square contains duplicate value
    kernal = [[[0,0],[1,0],[2,0]],
              [[0,1],[1,1],[2,1]],
              [[0,2],[1,2],[2,2]]]
    xprime = int(xpos/3)
    yprime = int(ypos/3)
    for row in kernal:
        for coord in row:
            coord[0] += (xprime * 3)
            coord[1] += (yprime * 3)
    for row in kernal:
        for coord in row:
            if puzzle[coord[1]][coord[0]] == n:
                return False

    return True


def solve(id,puzzle):
    for y in range(9):
        for x in range(9):
            if puzzle[y][x] == 0:
                for n in range(1,10):
                    if validator(x,y,n,puzzle):
                        puzzle[y][x] = n
                        solve(id,puzzle)
                        puzzle[y][x] = 0
                return
    np.savetxt(f'solutions/kaggle_solutions/{id}.csv',puzzle,fmt = '%d',delimiter=',')



def main():
    global puzzles_df
    for id in range(1,11):
        puzzle = setup_puzzle(id)
        solve(id, puzzle)

main()