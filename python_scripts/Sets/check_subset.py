t = int(input())

for _ in range(t):
    a_num = int(input())
    a = set(input().split())
    b_num = int(input())
    b = set(input().split())

    if a.issubset(b):
        print('True')
    else:
        print('False')