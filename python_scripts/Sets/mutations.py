a = int(input())
set_a = set(map(int, input().split()))
other = int(input())

for _ in range(other):
    operation = input()
    operation_name, count = operation.split()
    other_set = set(map(int, input().split()))

    if operation_name == 'intersection_update':
        set_a.intersection_update(other_set)
    elif operation_name == 'update':
        set_a.update(other_set)
    elif operation_name == 'symmetric_difference_update':
        set_a.symmetric_difference_update(other_set)
    else:
        set_a.difference_update(other_set)

total = sum(list(set_a))
print(total)
