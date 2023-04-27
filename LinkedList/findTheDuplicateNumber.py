class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        
        # identifying slow == fast
        while True:
            slow = nums[slow] 
            fast = nums[nums[fast]]
            if (slow == fast):
                break
        
        # find the meeting point
        slow = nums[0]
        while slow != fast:
            slow, fast = nums[slow], nums[fast]
            
        return slow
        
        