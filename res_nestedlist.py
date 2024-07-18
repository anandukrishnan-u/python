# a=[]
# b=[]
# c=[]
# if __name__ == '__main__':
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         a.append(name)
#         b.append(score)
#     set_list=sorted(list(set(b)))
#     sec_lowest=set_list[1]
#     #print(sec_lowest)
#     x=len(a)
#     nested_list=[]
#     nested_list=list(zip(a,b))
#     for i in range(x):
#         if nested_list[i][1]==sec_lowest:
#             c.append((nested_list[i][0]))
#     c.sort(reverse=True)
#     for i in c:
#         print(i)
            
a=[]
b=[]
c=[]
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        a.append(name)
        b.append(score)
    set_list=sorted(list(set(b)))
    sec_lowest=set_list[1]
    #print(sec_lowest)
    x=len(a)
    nested_list=[]
    nested_list=list(zip(a,b))
    for i in range(x):
        if nested_list[i][1]==sec_lowest:
            c.append((nested_list[i][0]))
    c.sort(reverse=True)
    for i in c:
        print(i)
            
