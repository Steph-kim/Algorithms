import random

def kth_greatest(arr, k):
    if not arr: return
    pivot = random.choice(arr)
    left = [i for i in arr if i > pivot]
    mid = [i for i in arr if i == pivot]
    right = [i for i in arr if i < pivot]
    
    L, M = len(left), len(mid)
    
    if k <= L:
        return kth_greatest(left, k)
    elif k > L + M:
        return kth_greatest(right, k - L - M)
    else:
        return mid[0]

