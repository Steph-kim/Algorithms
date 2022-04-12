def maxDifference(px):
    l = 0
    r = 1
    m = 0
    while r < len(px):
        curr = px[r] = px[l]
        if px[l] < px[r]:
            m = max(m, curr)
        else: 
            l = r
        r += 1
    return m if m != 0 else -1