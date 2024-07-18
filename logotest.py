# c='H'
# thickness=5
# i=2
# print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))
    
c='H'
print(c)
print(c).rjust(20)

for i in range(10):
    print((c*(i-1).ljust(5/i))+c+(c*(i-1).rjust(5/i)))