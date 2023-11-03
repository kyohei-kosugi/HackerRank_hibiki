import numpy as np

n = int(input())

array_list = []

for _ in range(n):
    array_list.append(list(map(float, input().split())))

print(round(np.linalg.det(array_list), 2))