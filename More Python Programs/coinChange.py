def count_coin_change_ways(coins, amount):
    dp = [0] * (amount + 1)
    
    dp[0] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]

coins = [1, 2, 3]
amount = 10
print(f"Number of ways to make change for {amount}:", count_coin_change_ways(coins, amount))
