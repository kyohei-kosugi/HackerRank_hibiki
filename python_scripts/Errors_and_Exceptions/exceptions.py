t = int(input())

for _ in range(t):
    a, b = input().split()
    try:
        print(int(int(a)/int(b)))
    except ZeroDivisionError as z:
        print("Error Code: integer division or modulo by zero")
    except ValueError as v:
        print("Error Code:", v)