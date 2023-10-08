from collections import deque
t = int(input())

for _ in range(t):
    n = int(input())
    blocks = list(map(int, input().split()))
    pile_list = deque()
    last = len(blocks) - 1

    for i in range(len(blocks)):
        
        if i == 0:
            pick_num = max(blocks[0], blocks[-1])
            pile_list.append(pick_num)
            blocks.remove(pick_num)
        elif i == last:
            print('Yes')
        else:
            pick_num = max(blocks[0], blocks[-1])
            if pick_num <= pile_list[i-1]:
                pile_list.append(pick_num)
                blocks.remove(pick_num)
            else:
                print('No')
                break


""" 
from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    blocks = list(map(int, input().split()))
    pile_list = deque()

    left, right = 0, n - 1

    while left <= right:
        if blocks[left] >= blocks[right]:
            pick_num = blocks[left]
            left += 1
        else:
            pick_num = blocks[right]
            right -= 1

        if not pile_list or pick_num <= pile_list[-1]:
            pile_list.append(pick_num)
        else:
            print('No')
            break

    if left > right:
        print('Yes')
 """