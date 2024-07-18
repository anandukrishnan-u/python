# # # n, m = map(int, input().split())
# # # lists = []

# # # for _ in range(n):
# # #     size, *elements = map(int, input().split())
# # #     lists.append(elements)

# # # max_value = 0

# # # def find_max_value(index, current_value):
# # #     global max_value

# # #     if index == n:
# # #         max_value = max(max_value, current_value % m)
# # #         return

# # #     for element in lists[index]:
# # #         find_max_value(index + 1, current_value + element**2)

# # # find_max_value(0, 0)
# # # print(max_value)

# # # if __name__ == '__main__':
# # #     n = int(input())
# # #     arr = map(int, input().split())

# # n=int(input())
# # l=[]
# # for i in range(n):
# #     x=int(input())
# #     l.append(x)

# # y=list(sorted(set(l)))
# # z=n-2
# # print(y[-2])
# nested_list = []

# if __name__ == '__main__':
#     for _ in range(int(input("Enter the number of students: "))):
#         name = input("Enter student's name: ")
#         score = float(input("Enter student's score: "))
#         nested_list.append([name, score])

# for i in range(len(nested_list)):
#     name = nested_list[i][1]
#     score = nested_list[i][0]
#     print("Student {}: Name: {}, Score: {}".format(i + 1, name, score))
# for i in range(10,0,-1):
#     print(i)
# a = []
# b = []

# if __name__ == '__main__':
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         a.append(name)
#         b.append(score)

#     unique_scores = sorted(set(b), reverse=True)
#     second_lowest = unique_scores[1]

#     nested_list = list(zip(a, b))
#     students_with_second_lowest = []

#     for i in range(len(nested_list)):
#         if nested_list[i][1] == second_lowest:
#             students_with_second_lowest.append(nested_list[i][0])

#     students_with_second_lowest.sort(reverse=True)  
#     for name in students_with_second_lowest:
#         print(name)

# c=[1,2,3]
# print(for i in c)
if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    students.sort(key=lambda x: x[1])

    second_lowest_score = sorted(set(score for name, score in students))[1]

    for name, score in students:
        if score == second_lowest_score:
            print(name)
