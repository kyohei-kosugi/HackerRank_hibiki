import numpy as np

n = int(input())

A = np.array([list(map(int, input().split())) for _ in range(n)])
B = np.array([list(map(int, input().split())) for _ in range(n)])

matrix = np.dot(A, B)


print(matrix)