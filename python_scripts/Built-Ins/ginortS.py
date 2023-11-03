import re

s = input()
sorted_text = ''.join(sorted(s))

digit_pattern = re.search(r'\d+', sorted_text)
upper_pattern = re.search(r'[A-Z]+', sorted_text)
lower_pattern = re.search(r'[a-z]+', sorted_text)

if digit_pattern:
    original_list = list(digit_pattern.group(0))
    odd_list = []
    even_list = []
    for letter in original_list:
        if int(letter) % 2 == 0:
            even_list.append(letter)
        else:
            odd_list.append(letter)
    digit_list = odd_list + even_list

if upper_pattern:
    upper_list = [upper_pattern.group(0)]

if lower_pattern:
    lower_list = [lower_pattern.group(0)]

result = lower_list + upper_list + digit_list
print(''.join(result))

""" 
s = input()

# 文字列をソートする
sorted_text = sorted(s)

# 数字、大文字、小文字を分類
digit_list = []
upper_list = []
lower_list = []

for char in sorted_text:
    if char.isdigit():
        digit_list.append(char)
    elif char.isupper():
        upper_list.append(char)
    elif char.islower():
        lower_list.append(char)

# 奇数と偶数の数字を分割
odd_list = [char for char in digit_list if int(char) % 2 != 0]
even_list = [char for char in digit_list if int(char) % 2 == 0]

# 結果を構築
result = lower_list + upper_list + odd_list + even_list

# 結果を出力
print(''.join(result))
 """