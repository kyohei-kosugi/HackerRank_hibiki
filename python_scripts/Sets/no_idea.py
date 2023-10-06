initial_num = map(int, input().split())

n_list = list(map(int, input().split()))
m1_list = list(map(int, input().split()))
m2_list = list(map(int, input().split()))

n_m1 = n_list + m1_list
n_m2 = n_list + m2_list
s1 = len(n_m1) - len(set(n_m1))
s2 = len(n_m2) - len(set(n_m2))

happy = s1 - s2

print(happy)

# for i in range(len(n_list)):
#     for j in range(len(m1_list)):
#         if m1_list[j] == n_list[i]:
#             happy += 1
#     for k in range(len(m2_list)):
#         if m2_list[k] == n_list[i]:
#             happy -= 1
