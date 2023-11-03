import numpy as np

n, m, p = map(int, input().split())

n_list = []
m_list = []

for _ in range(n):
    n_list.append(list(map(int, input().split())))

for _ in range(m):
    m_list.append(list(map(int, input().split())))

print(np.concatenate((np.array(n_list), np.array(m_list)), axis = 0))