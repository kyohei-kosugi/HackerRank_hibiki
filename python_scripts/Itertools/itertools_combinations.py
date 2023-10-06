from itertools import combinations

value, size = input().split()

for i in range(1, int(size)+1):
    word_combination = list(combinations(sorted(value), i))
    word_combination.sort()

    for j in range(len(word_combination)):
        print(''.join(word_combination[j]))