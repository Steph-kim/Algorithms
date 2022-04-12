def insert(intervals, newInterval):
    if not intervals: return [newInterval]
    res = []

    for i, interval in enumerate(intervals):
        if interval[0] < newInterval[1]:
            res.append([interval])
        else: 
            if interval[1] > newInterval[0]:
                return res + [newInterval] + intervals[i:]
            else:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1]) 
    
    return res + [newInterval]

