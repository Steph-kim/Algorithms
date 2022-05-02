def minCostClimbingStairs(cost):
    n = len(cost)
    dp = [0] * (n+1)

    for i in range(2, n+1):
        oneStep = dp[i-1] + cost[i-1]
        twoStep = dp[i-2] + cost[i-2]
        dp[i] = min(oneStep, twoStep)
    return dp[n]


