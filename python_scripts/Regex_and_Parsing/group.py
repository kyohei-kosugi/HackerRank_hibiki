import re

s = input()

pattern = r'([a-zA-Z0-9])\1+'

match = re.search(pattern, s)

if match:
    print(match.group(0)[0])
else:
    print('-1')