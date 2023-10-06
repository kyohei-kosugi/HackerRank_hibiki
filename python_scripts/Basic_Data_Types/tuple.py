# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

t = tuple(map(int, input().split()))
# print(t)
# print(type(t))

print(hash(t))