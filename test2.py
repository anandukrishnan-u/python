# def find_second_largest(n, numbers):
#     # Find the maximum number in the list
#     max_num = max(numbers)
    
#     # Remove all occurrences of the maximum number
#     unique_numbers = [num for num in numbers if num != max_num]
    
#     if len(unique_numbers) > 0:
#         # Find the maximum number from the remaining list, which will be the second-largest number
#         second_largest = max(unique_numbers)
#         return second_largest
#     else:
#         return None


# # Input the value of n
# n = int(input())

# # Input n numbers separated by spaces
# numbers_input = input()
# numbers = [int(x) for x in numbers_input.split()]

# # Call the function to find the second-largest number
# result = find_second_largest(n, numbers)

# # Print the result
# print(result)


n = int(input("Enter the value of n: "))
numbers_input = input()
numbers = list(map(int, numbers_input.split()))
print(numbers)
