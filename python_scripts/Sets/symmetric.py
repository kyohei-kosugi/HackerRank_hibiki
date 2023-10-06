e = int(input())
e_roll = set(map(int, input().split()))
f = int(input())
f_roll = set(map(int, input().split()))

symmetric_number = e_roll.symmetric_difference(f_roll)
print(len(symmetric_number))