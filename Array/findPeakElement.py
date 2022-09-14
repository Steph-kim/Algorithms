def findPeakElement(nums):
    l, r = 0, len(nums)-1

    while l < r:
        m = (l+r)//2
        print("this is before: ", l, r, m)

        if nums[m] > nums[m+1] and nums[m] > nums[m-1]:
            return m
        
        if nums[m] < nums[m+1]:
            l = m+1
        else: 
            r = m-1
            
        print("this is after: ", l, r, m)
        
    print(nums[l])
    return l

