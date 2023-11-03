import numpy as np

n, m = map(int, input().split())

matrix = []

for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

array = np.array(matrix)

print(np.mean(array, axis=1))
print(np.var(array, axis=0))
print(round(np.std(array, axis=None), 11))