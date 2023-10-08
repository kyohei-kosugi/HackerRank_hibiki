from collections import deque

n = int(input())
d = deque()
for _ in range(n):
    operation = input()
    if operation == 'pop':
        d.pop()
    elif operation == 'popleft':
        d.popleft()
    else:
        op_name, number = operation.split()
        if op_name == 'append':
            d.append((number))
        else:
            d.appendleft((number))

print(' '.join(d))


""" 
from collections import deque

n = int(input())
d = deque()

for _ in range(n):
    operation = input().split()
    op_name = operation[0]

    if op_name == 'pop':
        d.pop() if d else None
    elif op_name == 'popleft':
        d.popleft() if d else None
    else:
        number = operation[1]
        if op_name == 'append':
            d.append(number)
        elif op_name == 'appendleft':
            d.appendleft(number)

print(' '.join(d))
 """