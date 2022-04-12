from collections import defaultdict

def isAnagram(s, t):
    dic = {}
    for i in s:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    
    for j in t:
        if j not in dic:    
            return False
        else:
            dic[j] -= 1
    
    for val in dic.values():
        if val != 0:
            return False
    
    return True

def isAnagram2(s, t):
    if len(s) != len(t): return False
    st = sorted(t)
    
    for i, c in enumerate(sorted(s)):
        if c != st[i]: return False
    return True

def isAnagram3(s, t):
    return sorted(s) == sorted(t)

def isAnagram4(s, t):
    if len(s) != len(t):
        return False 
    count = defaultdict(int)
    for c in s:
        count[c] += 1
    for c in t:
        count[c] -= 1
        if count[c] < 0:
            return False
    return True