"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
"""

import math

def maxSubArray(nums):
        maxEnding = 0
        maxTillNow = -math.inf
        
        for i in range(len(nums)):     
            maxEnding += nums[i]
            if (maxEnding > maxTillNow):
                maxTillNow = maxEnding      
            if (maxEnding < 0):
                maxEnding = 0       
            
        return maxTillNow

# Another method
# def maxSubArray(nums):
#     for i in range(1, len(nums)):
#             if nums[i-1] > 0:
#                 nums[i] += nums[i-1]
#         return max(nums)

nums1 = [-2,1,-3,4,-1,2,1,-5,4]
nums2 = [-2, 1]
nums3 = [-1]
nums4 = [1]
nums5 = [-2,-1,-3]
nums6 = [5,4,-1,7,8]
print(maxSubArray(nums1))
print(maxSubArray(nums2))
print(maxSubArray(nums3))
print(maxSubArray(nums4))
print(maxSubArray(nums5))
print(maxSubArray(nums6))
