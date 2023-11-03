import numpy as np

params = tuple(map(int, input().split()))

zero_array = np.zeros((params), int)
one_array = np.ones((params), int)

print(zero_array)
print(one_array)

