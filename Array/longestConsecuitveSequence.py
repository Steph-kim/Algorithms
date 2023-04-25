def longestConsecutive(nums):
    nums = set(nums)
    best = 0

    for x in nums:
        if x-1 not in nums:
            y = x+1
            while y in nums:
                y += 1
            best = max(best, y-x)
    return best

        # def seq_length(num):
        #     if num not in unique: 
        #         return 0
        #     unique.remove(num)
        #     length = seq_length(num-1) + seq_length(num+1)
        #     return length + 1
         
        # unique = set(nums)
        # max_length = 0

        # while unique and len(unique) > max_length:
        #     popped = unique.pop()
        #     unique.add(popped)
        #     length = seq_length(popped)
        #     max_length = max(max_length, length)
        # return max_length
