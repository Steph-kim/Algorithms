import math

def maxProduct(nums):
    maxProd = nums[0]
    minProdEnd = nums[0]
    maxProdEnd = nums[0]
    
    for i in range(1, len(nums)):
        a = min(nums[i], minProdEnd*nums[i], maxProdEnd*nums[i])
        b = max(nums[i], minProdEnd*nums[i], maxProdEnd*nums[i])

        minProdEnd, maxProdEnd = a, b
        maxProd = max(maxProd, maxProdEnd)

    return maxProd