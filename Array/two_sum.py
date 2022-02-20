"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

def twoSum(nums, target):

    dict = {}

    for count, num in enumerate(nums):
        v = target - num
        if v in dict:
            return [count, dict[v]]
        dict[num] = count

nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))