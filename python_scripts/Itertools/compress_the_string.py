from itertools import groupby

s = input()
initial_list = []

for i in s:
    initial_list.append(i)

groups = groupby(initial_list, key=lambda x: x[0])


for key, group in groups:
    count = len(list(group))
    print((count, int(key)), end=' ')


from itertools import groupby

""" S = input()

for k, g in groupby(S):
    t = (len(list(g)), int(k))
    print(t, end=" ") """
    