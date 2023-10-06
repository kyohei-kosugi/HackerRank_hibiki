from collections import namedtuple

student_num = int(input())
Score = namedtuple('Score', map(str, input().split()))

index = []
for _ in range(student_num):
    data = input().split()
    index.append(Score(*data))

total_scores = 0
for i in range(student_num):
    total_scores += int(index[i].MARKS)

average = float(total_scores / student_num)
print(round(average, 3))
