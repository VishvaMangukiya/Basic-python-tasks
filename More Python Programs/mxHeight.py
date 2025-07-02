def max_coin_triangle_height(N):
    if N < 1:
        return 0
    
    height = 0
    coins_used = 0
    
    while True:
        height += 1
        coins_needed = height * (height + 1) // 2
        if coins_needed > N:
            return height - 1
        if coins_needed == N:
            return height

N = int(input("Enter the number of coins: "))
print("Maximum height of the triangle:", max_coin_triangle_height(N))