# Single traversal
# Time complexity: O(n)
def findTwoLargest(nums):
    if len(nums) < 2: 
        return
    
    first = second = float('-inf')
    for i in range(len(nums)):
        if nums[i] > first:
            second = first
            first = nums[i]
        elif nums[i] > second and nums[i] != first:
            second = nums[i]

    return (second, first)

test1 = [12, 35, 1, 10, 34, 1]
print(findTwoLargest(test1))

test2 = [-2, -3, 1, -15, -4, -1, 1]
print(findTwoLargest(test2))
