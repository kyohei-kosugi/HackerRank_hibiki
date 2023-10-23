a = set(input().split())
n = int(input())

set_list = []

for _ in range(n):
    other_set = set(input().split())
    set_list.append(other_set)

for i in range(len(set_list)):
    if a.issuperset(set_list[i]):
        if i == len(set_list) -1:
            print('True')
        continue
    else:
        print('False')
        break
