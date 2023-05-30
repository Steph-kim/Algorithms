class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        s = 0
        dic = {0:-1}
        for i in range(len(nums)):
            s = (s + nums[i]) % k
            if s in dic:
                if i - dic[s] >= 2:
                    return True 
            else:
                dic[s] = i

        return False
