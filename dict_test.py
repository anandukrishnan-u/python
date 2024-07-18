# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
    
#     print(student_marks[name])

   # return my_dict

if __name__ == '__main__':
     
     n = int(input())
     my_dict = {}
     for _ in range(n):
        key, *values = input().split()
        
        my_dict[key] = values

        print(my_dict)


    