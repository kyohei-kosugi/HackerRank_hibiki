import re

s = input()
k = input()

matches = re.finditer(rf'(?=({k}))', s)

found = False

for match in matches:
    print((match.start(1), match.end(1) -1))

    found = True

if not found:
    print((-1, -1))