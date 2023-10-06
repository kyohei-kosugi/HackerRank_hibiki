from collections import Counter

k = int(input())
room_list = list(map(int, input().split()))

group_counts = Counter(room_list)

for group, count in group_counts.items():
    if count == 1:
        print(group)
