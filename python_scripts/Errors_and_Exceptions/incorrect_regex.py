import re

t = int(input())

for _ in range(t):
    case = str(input())

    try:
        re.compile(case)
        print('True')
    except re.error:
        print('False')
