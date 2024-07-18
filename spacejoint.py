s=input()
x=s.replace(' ','-')
print(x)




# def split_and_join(line):
#     # write your code here

# if __name__ == '__main__':
#     line = input()
#     result = split_and_join(line)
#     print(result)

# s='hello'
# print(s)
# l=list(s)
# print(l)
# c=''.join(l)
# print(c)
if __name__ == '__main__':
    s = input()
    
    for char in s:
        
        if(s.alnum()):
            print("True")
        else:
            print("False")