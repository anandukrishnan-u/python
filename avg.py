if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
       # print(line)
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    if query_name in student_marks:
     query_value=student_marks.get(query_name)
     num=len(query_value)
     sum_value=sum(student_marks.get(query_name,0))    
    #print(sum_value)
    res=sum_value/num
    print(f'{res:.2f}')
    