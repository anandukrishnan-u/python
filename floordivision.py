# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read input values for each test case
    lower_limit, sticks_per_plate, money_received = map(int, input().split())
    
    # Calculate the number of extra sticks Chef ate
    extra_sticks = money_received // 30
    
    # Calculate the total number of sticks Chef ate
    total_sticks = lower_limit + extra_sticks
    
    # Calculate the maximum number of plates Chef could have ordered
    max_plates = (total_sticks + sticks_per_plate - 1) // sticks_per_plate
    
    print(max_plates)
