from itertools import combinations

n = int(input())
letter_list = list(input().split())
k = int(input())

letter = 'a'

combinations_list = list(combinations(letter_list, k))
count = 0

for comb in combinations_list:
    if 'a' in comb:
        count += 1
print(round(count/len(combinations_list), 4))
