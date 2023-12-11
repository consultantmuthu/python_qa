if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    score_list = student_marks.get(query_name)
    average = 0.00
    for i in range(len(score_list)):
        average = average + score_list[i]
    
    if average > 0:
        average = average / len(score_list)
    print(format(average, '.2f'))