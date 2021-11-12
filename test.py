import numpy as np

newBoard = np.zeros((8,8))

for i in range(8):
    for j in range(8):
        newBoard[i,j] = input(("Digit the number of column " + str(j + 1) + " row " + str(i + 1) + ": "))
       
print(newBoard)
