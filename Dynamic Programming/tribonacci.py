def tribonacci(n):
    # if n == 0: 
    #     return 0
    
    # if n == 1 or n == 2:
    #     return 1
    
    # return self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)

    if n < 2:
        return n
    
    t0 = 0
    t1 = t2 = 1 
    tn = 0

    for i in range(n-2):
        tn = t0 + t1 + t2 
        t0 = t1 
        t1 = t2 
        t2 = tn

    return t2

    