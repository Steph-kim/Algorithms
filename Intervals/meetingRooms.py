def canAttendMeetings(intervals):
    intervals.sort()
    lastEnd = intervals[0][1]

    for start, end in intervals:
        if (start < lastEnd):
            return False
        
    return True