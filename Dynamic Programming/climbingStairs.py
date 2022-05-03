"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

"""

# Bottom up approach  
# Time complexity: O()
def climbStairs(n):
    if n == 1: 
        return 1
    
    dp = [0 for _ in range(n)]
    dp[0], dp[1] = 1, 2
    
    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]
        
    return dp[-1]

# Iterative approach
# For any given step, you can reach it from (n-2) steps away or (n-1) steps away.
# Therefore, the total number of ways to get to n is the sum of the total number of ways to get to (n-2)
# and the total number of ways to get to (n-1)
# Essentially fibonacci sequence where:
#   a represents (n-2)
#   b represents (n-1)
# Time complexity: O(n)
def climbStairs2(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return a