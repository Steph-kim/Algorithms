from heapq import heapify, heappop, heappush

def reductionCost(num):
    res = 0
    heapify(num)
    while len(num) > 1:
        a, b = heappop(num), heappop(num)
        sum = a + b
        res += sum
        heappush(num, sum)
    return res
