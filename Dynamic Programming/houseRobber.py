# https://leetcode.com/problems/house-robber/solutions/156523/from-good-to-great-how-to-approach-most-of-dp-problems/

class Solution:

    """

    [2,7,9,3,1]

    Find the recurrence relation.
    ----------------------------------------------------------
    In each house we are at, the robber can make two choices:
    
    1. rob the current house
        take the money and move down two houses
        nums[i] + rob(n-2)
    
    2. dont rob the current house
        move down one house
        rob(n-2)

    What it comes down to is which is more profitable.
    This can be represented using the following:

    rob(i) = max(rob(i-2) + nums[i], rob(i-2))


    """
    def rob(self, nums: List[int]) -> int:
        # memo = [-1] * len(nums)
        # def robRecur(i): 
        #     if i < 0:
        #         return 0

        #     if memo[i] > 0:
        #         return memo[i]

        #     res = max(robRecur(i-2) + nums[i], robRecur(i-1))
        #     memo[i] = res
        #     return res

        # return robRecur(len(nums)-1)


        memo = [-1] * (len(nums) + 1)
        memo[0] = 0
        memo[1] = nums[0]

        for i in range(1, len(nums)):
            memo[i+1] = max(memo[i-1] + nums[i], memo[i])

        return memo[len(nums)]

    
        # num1 = 0
        # num2 = 0

        # for i in range(0, len(nums)):
        #     tmp = num1
        #     num1 = max(num2 + nums[i], num1)
        #     num2 = tmp
        # return num1