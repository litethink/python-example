import copy
import numpy as np
from data import sudoku
# sudoku = [
#     [1,0,0,4,0,0],
#     [3,0,0,5,0,2],
#     [0,0,1,0,0,0],
#     [2,0,0,3,0,0],
#     [4,0,0,0,0,3],
#     [0,0,3,6,0,0]
# ]

#Twelfth order
# sudoku = [
# [0,0,0,0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,0,0,0,8]
# ]

# sudoku = [

# [0,0,0,0,0,0,2,0,0],
# [0,0,0,3,0,0,0,1,0],
# [0,0,9,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,9,0],
# [0,0,0,0,1,0,0,0,0],
# [0,0,5,0,0,3,0,0,0],
# [0,2,0,0,0,0,4,0,0],
# [0,0,0,0,0,0,0,6,0],
# [0,0,0,0,0,0,0,0,8]
# ]


def check_data(sudoku):
    if not isinstance(sudoku,list):
        print("Type is not List type.")
        exit()

    x = np.array(sudoku)
    if len(x.shape) != 2:
        print("Shape dimension ineffective.")
        exit()

    if x.shape[0] != x.shape[1] :
        print("Dimension effective but shape misaligned.")
        
        exit()

    if x.dtype != "int":
        print("Sudoku data type is not effective.")
        exit()
    sudoku_length = len(x)
    for i in x:
        if (i > sudoku_length).any():
            print("Value override maximal.")
            exit()
        if len(i[i>0]) != len(set(i[i>0])):
            print("Row value have to no repeat.")
            exit()
    for j in x.transpose():
        if len(j[j>0]) != len(set(j[j>0])):
            print("Column value have to no repeat.")
            exit()
    return x

def get_unknown_position(x):
    sudoku_length = len(x)
    sudolen = range(len(x))
    l = []
    for i in sudolen:
        for j in sudolen:
            if x[i][j] == 0:
                l.append([i,j])
    return l

def check_result(img_x):
    for i in img_x:
        if 0 in i:
            return False
    return True

def solve_soduku(x,freq=1000000):
    numset = set(range(1,len(x)+1))
    posi = get_unknown_position(x)
    while True:
        freq -= 1
        img_x = copy.copy(x)
        for i,j in posi:
            y = img_x.transpose()
            choices = list(numset.difference(set(img_x[i]).union(y[j])))
            if not choices:
                continue
            img_x[i][j] = np.random.choice(choices)

        result = check_result(img_x)
        if result:
            return img_x,None
        if freq  == 0:
            return False,"No answer."


if __name__ == '__main__':

    x = check_data(sudoku)

    result,err = solve_soduku(x)
    if not err:
        print(result)
    else:
        print("Maybe no answer or solve with frequency insufficient.")
