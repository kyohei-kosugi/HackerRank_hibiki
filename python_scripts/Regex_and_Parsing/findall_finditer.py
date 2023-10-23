import re

s = input()

vowel_pattern = r'(?=([^aeiouAEIOU][aeiouAEIOU]{2,}[^aeiouAEIOU]))'

matches = re.finditer(vowel_pattern, s)

found = False

for match in matches:
    vowel_seq = match.group(1)[1:-1]
    print(vowel_seq)
    found = True

if not found:
    print(-1)