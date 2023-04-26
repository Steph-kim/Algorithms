"""
Question:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

*** simple hashmap / dict solution. ***

The key to this problem is that there is exactly ONE pair of numbers that will sum to the given target.
We can assume that for all the numbers in the list [x1, x2, x3, ..., xn], 
there exists a pair such that xa + xb = target.

To solve this question with a single loop, we can change the equation above to xa = target - xb 
where 
    xb = current element we are at.
    xa = pair we want to look for to reach the target.

By using a hashmap, we can keep a record of all the previous values we have seen so far and check whether xa exists in the record.
If xa does not exist in the hashmap, then we store it as a key in the hashmap where the value will be the index it was seen at.

If xa does exist in the hashmap, then we have found a matching pair and we return the indexes as such:
    [current index, dict[xa]]
where dict[xa] gives the index of where xa was seen.

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