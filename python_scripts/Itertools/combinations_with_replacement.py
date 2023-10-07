from itertools import combinations_with_replacement

s = input()
character, count = s.split()

character_list = sorted(list(character))

result = sorted(list(combinations_with_replacement(''.join(character_list), int(count))))

for word in result:
    print(''.join(word))
