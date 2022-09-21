def sumEvenAfterQueries(nums, queries):
    
    res = []
    s = sum(num for num in nums if num%2 == 0)
    
    for val, index in queries:
        if nums[index] % 2 == 0:
            s -= nums[index] 
        nums[index] += val
        if nums[index] % 2 == 0:
            s += nums[index]
        res.append(s)
    
    return res