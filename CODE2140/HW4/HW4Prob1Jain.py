import numpy as np

def common_elements(A, mode=0):
    num_rows, num_cols = A.shape
    if mode == 1:
        vals = set(A.T[0])
        for i in range(1, num_rows):
            row_vals = set(A[i])
            vals = vals.intersection(row_vals)
    elif mode == 1:
        A_t = A.T
        vals = set(A_t[0])
        for i in range(1, num_cols):
            col_vals = set(A_t[i])
            vals = vals.intersection(col_vals)
    else:
        return 'Invalid mode. Enter 0 for row-wise and 1 for column-wise.'
    
    return vals


A = np.array([[7, 1, 5, 6],
[2, 6, 1, 1],
[6, 1, 7, 2],
[6, 6, 3, 1],
[5, 5, 6, 1],
[3, 6, 7, 1]])
print(common_elements(A))