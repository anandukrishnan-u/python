t = int(input())

for _ in range(t):
    n = int(input())  

    purchased_gifts = n // 4 * 4
    free_gifts = n // 4

    total_cost = purchased_gifts + free_gifts
    remaining_gifts = n % 4
    if remaining_gifts == 1:
        total_cost += 1
    elif remaining_gifts > 1:
        total_cost += 4

    print(total_cost)
