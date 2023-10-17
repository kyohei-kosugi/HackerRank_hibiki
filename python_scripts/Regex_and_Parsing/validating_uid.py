import re

t = int(input())

for _ in range(t):
    uid = input()
    if len(set(uid)) == len(list(uid)):
        uid_pattern = r'^(?=(?:.*[A-Z]){2})(?=(?:.*[0-9]){3})[A-Za-z0-9]{10}$'
        match = re.match(uid_pattern, uid)
        if match:
            print('Valid')
        else:
            print('Invalid')
    else:
        print('Invalid')