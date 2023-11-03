import numpy as np

n, m = map(int, input().split())

a_list = []
b_list = []

for _ in range(n):
    a_list.append(list(map(int, input().split())))

for _ in range(n):
    b_list.append(list(map(int, input().split())))

a_array = np.array(a_list)
b_array = np.array(b_list)

print(np.add(a_array, b_array))
print(np.subtract(a_array, b_array))
print(np.multiply(a_array, b_array))
print(np.divide(a_array, b_array).astype(int))
print(np.mod(a_array, b_array))
print(np.power(a_array, b_array))