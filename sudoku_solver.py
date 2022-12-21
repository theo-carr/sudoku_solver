#imports
import pandas as pd
import numpy as np

def loadPuzzles(difficulty):  #difficulty takes the sheet name of the excel file; easy, medium, hard, expert, and evil
    puzzle = pd.read_excel('puzzles/puzzles.xlsx', header=None, sheet_name=difficulty)
    return puzzle.to_numpy()

easyPuzzle = loadPuzzles('easy')
mediumPuzzle = loadPuzzles('medium')
hardPuzzle = loadPuzzles('hard')
expertPuzzle = loadPuzzles('expert')
evilPuzzle = loadPuzzles('evil')

mode = input("Please Enter A Difficulty: ")
mode = mode.lower()
if mode == 'easy':
    puzzle = easyPuzzle
elif mode == 'medium':
    puzzle = mediumPuzzle
elif mode == 'hard':
    puzzle = hardPuzzle
elif mode == 'expert':
    puzzle = expertPuzzle
elif mode == 'evil':
    puzzle = evilPuzzle
else:
    print('invalid input')


def validator(xpos, ypos, n):
    global puzzle
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
    #print(f'kernal:\n{kernal}')
    #else return true
    return True

def solve():
    global puzzle
    for y in range(9):
        for x in range(9):
            if puzzle[y][x] == 0:
                for n in range(1,10):
                    if validator(x,y,n):
                        puzzle[y][x] = n
                        solve()
                        puzzle[y][x] = 0
                return
    np.savetxt(f'solutions/{mode}.csv',puzzle,fmt = '%d',delimiter=',')

def main():
    global puzzle
    print(f'unsolved puzzle = \n{puzzle}')
    solve()
    solved_puzzle = pd.read_csv(f'solutions/{mode}.csv', header=None)
    print(solved_puzzle)



main()