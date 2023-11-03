import numpy as np

n, m = map(int, input().split())

matrix = []

for _ in range(n):
    matrix.append(input().split())

array = np.array(matrix, int)

sum = np.sum(array, axis=0)
print(np.prod(sum))