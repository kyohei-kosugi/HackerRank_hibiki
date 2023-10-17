import re

n = int(input())

line = 0

while line < n:
    selector = input().strip()
    line += 1

    if not selector:
        continue

    while True:
        sentense = input()
        
        if sentense != '}':
            css_pattern = r"#[a-fA-F0-9]{3}([a-fA-F0-9]{3})?"
            pattern_match = re.finditer(css_pattern, sentense)

            for match in pattern_match:
                matched_text = match.group(0)
                print(matched_text)
            line += 1
        else:
            line += 1
            break
