import re

t = int(input())
pattern = r'^[+-]?[0-9]*\.{1}[0-9]+$'
# ^[+-]?\d*\.\d+$

for _ in range(t):
    number = input()
    match = re.search(pattern, number)
    if match:
        print('True')
    else:
        print('False')