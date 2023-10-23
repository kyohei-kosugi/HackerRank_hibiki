import re

n = int(input())

for _ in range(n):
    phone_number = input()
    pattern = r"^[7|8|9]\d{9}"

    match = re.match(pattern, phone_number)

    if len(phone_number) > 10:
        print("NO")
    else:
        if match:
            print("YES")
        else:
            print("NO")