def lengthOfLongestSubstring(str):
    dict = {}
    start = maxLen = 0
    
    for i, c in enumerate(s):
        if (c in dict and start<=dict[c]):
            start = dict[c]+1
        else:
            maxLen = max(maxLen, i-start+1)
        dict[c] = i
            
    return maxLen