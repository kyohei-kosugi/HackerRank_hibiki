e = int(input())
e_roll = set(map(int, input().split()))
f = int(input())
f_roll = set(map(int, input().split()))

difference_number = e_roll.difference(f_roll)
print(len(difference_number))