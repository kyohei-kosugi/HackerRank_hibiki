import numpy as np
np.set_printoptions(legacy='1.13')

n, m = map(int, input().split())

array = np.eye(n, m)

print(array)