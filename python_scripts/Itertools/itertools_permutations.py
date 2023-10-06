from itertools import permutations

value, size = input().split()

word_combination = list(permutations(list(value), int(size)))
word_combination.sort()

for i in range(len(word_combination)):
    print(''.join(word_combination[i]))
