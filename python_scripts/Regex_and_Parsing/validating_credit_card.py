import re

n = int(input())

for _ in range(n):
    card_number = input()
    
    num_pattern = r'^[4-6]\d{3}-?\d{4}-?\d{4}-?\d{4}$'
    num_match = re.match(num_pattern, card_number)

    only_number = card_number.replace("-", "")
    repeat_pattern = r'(\d)\1{3,}'
    repeat_match = re.search(repeat_pattern, only_number)

    if not repeat_match:
        if num_match:
            print('Valid')
        else:
            print('Invalid')
    else:
        print('Invalid')