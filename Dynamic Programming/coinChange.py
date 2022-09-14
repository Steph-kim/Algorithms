def coinChange(coins, amount):
    dp = [0] + [float('inf') for _ in range(amount)]

    for i in range(1, amount+1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i-coin] + 1)

    return dp[-1] if dp[-1] != float('inf') else -1


