def isValid(s):
    dict = {
        "]":"[",
        ")":"(",
        "}":"{",
    }
    stack = []
    
    for c in s:                     
        if c in dict.values():
            stack.append(c)                
        else:
            if stack == [] or dict[c] != stack.pop():
                return False
    return not stack