n, x = map(int, input().split())

all_students_score = []
for _ in range(x):
    all_score = list(map(float, input().split()))
    all_students_score.append(all_score)

subjects_list = list(zip(*all_students_score))

for i in range(n):
    total_score = 0

    for score in subjects_list[i]:
        total_score += score

    print(round((total_score / x), 1))

""" 
for subject_scores in subjects_list:
    average_score = round(sum(subject_scores) / x, 1)
    print(average_score)
     """