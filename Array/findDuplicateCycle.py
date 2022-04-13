def findDuplicate(nums):
    if (len(nums) <= 1): return -1
    
    slow = nums[0]
    fast = nums[nums[0]]
    
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]
                    
    fast = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow
                       