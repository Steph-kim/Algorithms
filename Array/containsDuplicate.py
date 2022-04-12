"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""

# Single line solution using sets
def containsDuplicate(nums):
    return len(nums) != len(set(nums))

# Use set O(n)
def containsDuplicate2(nums):
    set_List = set()
    for num in nums:
        if (num in set_List):
            return True
        set_List.add(num)
    return False

# Applying hashtable O(n)
def containsDuplicate3(nums):
    dict = {}
    for num in nums:
        if num in dict:
            return True
        dict[num] = num
    return False

# Using sort O(nlogn) -> timesort is O(nlogn)
def containsDuplicate4(nums):
    l = len(nums)
    if (l < 2):
        return False
    nums.sort()
    for i in range(l-1):
        if (nums[i] == nums[i+1]):
            return True
    return False

nums = [1,2,3,1]
nums2 = [1,2,3,4]
nums3 = []
nums4 = [1]

print(containsDuplicate(nums))
print(containsDuplicate(nums2))
print(containsDuplicate(nums3))
print(containsDuplicate(nums4))
print()

print(containsDuplicate2(nums))
print(containsDuplicate2(nums2))
print(containsDuplicate2(nums3))
print(containsDuplicate2(nums4))
print()

print(containsDuplicate3(nums))
print(containsDuplicate3(nums2))
print(containsDuplicate3(nums3))
print(containsDuplicate3(nums4))
print()

print(containsDuplicate4(nums))
print(containsDuplicate4(nums2))
print(containsDuplicate4(nums3))
print(containsDuplicate4(nums4))