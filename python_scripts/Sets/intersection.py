e = int(input())
e_roll = set(map(int, input().split()))
f = int(input())
f_roll = set(map(int, input().split()))

intersection_number = e_roll.intersection(f_roll)
print(len(intersection_number))