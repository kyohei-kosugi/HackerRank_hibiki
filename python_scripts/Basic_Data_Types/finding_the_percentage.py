if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        ## *line means it includes all items after the second
        name, *line = input().split()
        ## map(float, line) transfers value in line to float
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    marks = student_marks[f'{query_name}']
    total_score = 0
    for i in range(3):
        total_score += marks[i]
    
    result = "{:.2f}".format(total_score /3)
    print(result)
