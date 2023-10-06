e = int(input())
e_roll = set(map(int, input().split()))
f = int(input())
f_roll = set(map(int, input().split()))

union_number = e_roll.union(f_roll)
print(len(union_number))