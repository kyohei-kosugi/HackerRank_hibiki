n = int(input())
s = set(map(int, input().split()))
n_commands = int(input())

for _ in range(n_commands):
    command = input()
    if command == 'pop':
        s.pop()
    else:
        c, count = command.split()
        if c == 'remove':
            s.remove(int(count))
        else:
            s.discard(int(count))

sum = 0
for i in s:
        sum += i
print(sum)
