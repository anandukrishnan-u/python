n = int(input())
for i in range(n):
    (a, b, c) = map(int, input().split())
    x = c / 30
    if x >= 1 & b!=1:
        print(((a + x) // b)+1)
    elif x>=1 and b==1:
        print(x+a)
    else:
        print((a // b)+1)
