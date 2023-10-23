import re

n = int(input())

for _ in range(n):
    text = input()

    while ' && ' in text:
        text = re.sub(r'\s&&\s', ' and ', text)
    while ' || ' in text:
        text = re.sub(r'\s\|\|\s', ' or ', text)

    print(text)