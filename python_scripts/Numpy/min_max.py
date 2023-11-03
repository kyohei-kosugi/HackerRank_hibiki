import numpy as np

n, m = map(int, input().split())

matrix = []

for _ in range(n):
    matrix.append(input().split())

array = np.array(matrix, int)
min_value = np.min(array, axis=1)
max_value = np.max(min_value)

print(max_value)