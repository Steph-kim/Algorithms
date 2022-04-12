def eraseOverlapIntervals(intervals):
    if not intervals: return 0
    
    intervals.sort(key=lambda x: x[0])
    lastEnd = intervals[0][1]
    overlaps = 0
    
    for start, end in intervals[1:]:
        if (start < lastEnd):
            overlaps += 1
            lastEnd = min(lastEnd, end)
        else:
            lastEnd = end
            
    return overlaps
