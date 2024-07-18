# n=int(input())
# leap=False
# #if n%4==0:
# if n%100==0 and n%400==0:
#         leap = True
# if n%4==0 and n%100!=0:
#         leap=True
# else:
#    leap = False
# print(leap)

n=int(input())
leap=False
if n%4==0 and n%100==0 and n%400==0:
    leap = True
elif n%4==0 and n%100!=0:
    leap=True
print(leap)