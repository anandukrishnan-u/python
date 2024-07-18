# cook your dish here
n=int(input())
for i in range(n):
     x=int(input())
     if x<=4:
         print(x)
     elif x==5:
        print("4")
     else:
         a=(x%4)+(x//4)
         print(x-a)