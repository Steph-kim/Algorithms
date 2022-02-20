"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""

# Logic:
# The first loop saves all the prefix values multiplied.
# The second loop multiplies all the postfix values with the prefix values to get the final solution. 
def productExceptSelf(nums):

    result = [1]*len(nums)
    product = 1

    for i in range(len(nums)):
        result[i] *= product
        product *= nums[i]

    product = 1

    for i in range(len(nums)-1, -1, -1):
        result[i] *= product
        product *= nums[i]

    return result

# Same logic as solution above
def productExceptSelf2(nums):

    left = [0]*len(nums)
    right = [0]*len(nums)
    result = [0]*len(nums)

    left[0] = 1
    right[len(nums)-1] = 1

    for i in range(1, len(nums)):
        left[i] = nums[i-1] * left[i-1]

    for i in range(len(nums)-2, -1, -1):
        right[i] = nums[i+1] * right[i+1]

    for i in range(len(nums)):
        result[i] = left[i]*right[i]

    return result

"""
// All in one solution
class Solution:
    def productExceptSelf(self, nums):
        
        :type nums: List[int]
        :rtype: List[int]
        
        res = [1]*len(nums)
        lprod = 1
        rprod = 1
        for i in range(len(nums)):
            res[i] *= lprod
            lprod *= nums[i]
            res[~i] *= rprod
            rprod *= nums[~i]
        return res
"""

nums1 = [-1,1,0,1,-3,3]
nums2 = [1,2,3,4]
print(productExceptSelf(nums1))
print(productExceptSelf2(nums1))

print(productExceptSelf(nums2))
print(productExceptSelf2(nums2))

