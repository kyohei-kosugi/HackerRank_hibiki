import re

def wrapper(f):
    def fun(l):
        # complete the function
        zero_pattern = r'^[0][0-9]{10}$'
        add_91_pattern = r'^\+?91[0-9]{10}$'
        ten_pattern = r'^[0-9]{10}$'

        valid_numbers = []

        for number in l:
            z_match = re.match(zero_pattern, number)
            a_match = re.match(add_91_pattern, number)
            t_match = re.match(ten_pattern, number)

            if z_match:
                formatted_number = re.sub(r'^0', '+91 ', number)
                valid_numbers.append(' '.join(re.findall(r'\+?\d{1,5}', formatted_number)))
            elif a_match:
                formatted_number = re.sub(r'^\+?91', '+91 ', number)
                valid_numbers.append(' '.join(re.findall(r'\+?\d{1,5}', formatted_number)))
            elif t_match:
                formatted_number = '+91 '  + number
                valid_numbers.append(' '.join(re.findall(r'\+?\d{1,5}', formatted_number)))
        
        f(valid_numbers)

    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)


