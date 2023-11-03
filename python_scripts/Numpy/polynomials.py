import numpy as np

p = list(map(float, input().split()))
x = int(input())

poly = np.polyval(p, x)
print(poly)