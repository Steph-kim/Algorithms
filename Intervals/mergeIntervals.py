def merge(intervals):
    if not intervals: return [intervals]
    
    intervals.sort(key = lambda x: x[0])
    output = [intervals[0]]

    for start, end in intervals[1:]:
        lastEnding = output[-1][1]
        if start <= lastEnding:
            output[-1][1] = max(end, lastEnding)  
        else: 
            output.append([start, end])
    
    return output
        