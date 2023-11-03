import numpy as np

n, m = map(int, input().split())

initial_array = []

for _ in range(n):
    initial_array.append(list(map(int, input().split())))

print(np.transpose(initial_array))
print(np.array(initial_array).flatten())