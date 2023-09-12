import numpy as np

A = np.arange(2.0, 19.0, 2).reshape(3,3)
B = np.arange(9.0, 0.0, -1).reshape(3, 3)
print(f'Matrix A:\n{A}\n')
print(f'Matrix B:\n{B}\n')
print(f'A^2:\n{A ** 2}\n')
print(f'Element-wise multiplication:\n{(A ** 2) * B}\n')
print(f'Matrix-wise multiplication:\n{(np.dot(A ** 2, B))}\n')

A[B % 3 == 0] = np.sqrt(A[B % 3 == 0])
print(f'New A:\n{A}\n')
B[A % 4 == 0] = -1 * B[A % 4 == 0]
print(f'New B:\n{B}\n')

a_inv = np.linalg.inv(A)
b_inv = np.linalg.inv(B)

print("A inverse times B inverse:")
print(f'Element-wise:\n{a_inv * b_inv}\n')
print(f'Matrix-wise:\n{np.dot(a_inv, b_inv)}\n')