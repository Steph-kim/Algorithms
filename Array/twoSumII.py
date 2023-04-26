"""
Explanation:

*** Two pointers technique. ***

The array is sorted in increasing order.
Increasing the left index gives a bigger number
Increasing the right index gives a smaller number

First initialise the left and right pointers to the 0th index and the last index of the array respectively.

We need to check two things: 

Let the sum = numbers[l] + numbers[r]

1. If the sum is less than the target, then we have to increase the sum. To do this, we increment the left index.
2. If the sum is greater than the target, then we have to decrease the usm. To do this we decrement the right index.
3. If the sum is equal to the target, then we return the index (+1 since the solution works on a 1th index basis).

"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                return [l+1, r+1]
