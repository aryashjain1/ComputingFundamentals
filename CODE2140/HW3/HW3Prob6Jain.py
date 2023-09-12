import numpy as np

def slope_elements(A):
    num_rows, num_cols = A.shape
    
    iters_cols, iters_rows = 0, 0
    if num_rows > num_cols:
        iters_cols = num_cols
        iters_rows = num_rows - 1
    else:
        iters_cols = num_cols - 1
        iters_rows = num_rows

    #Upper triangle
    for i in range(iters_cols):
        for j in range(i+1):
            print(A[j][num_cols-1-i+j], end = "\t")
        print()
    #Lower Triangle
    for i in range(iters_rows, -1, -1):
        for j in range(i):
            print(A[num_rows-i+j][j], end = "\t")
        print()

A = np.linspace(1, 25, num=25)
A = np.reshape(A, (5, 5))
print(A)
slope_elements(A)