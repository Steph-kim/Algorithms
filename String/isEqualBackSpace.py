# Time complexity: O(n^2)
# res[:-1] operation is O(n) as it copies the array into a new array 

def backspaceCompare(s1, s2):
    def backSpace(s):
        res = []
        for c in s:
            if c != '#':
                res.append(c)
            else:
                res = res[:-1]
        return res
    return backSpace(s1) == backSpace(s2)

s1 = "hn#ll#el"
s2 = "hlel#l"
print(backspaceCompare(s1, s2))

# Using a stack
# Time complexity: O(m+n)
# Space complexity: O(m+n)
def backspaceCompare2(s1, s2):
    def backSpace(s):
        stack = []
        for c in s:
            if c == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
    return backSpace(s1) == backSpace(s2)

print(backspaceCompare2(s1, s2))

# Reverse iterator
# Time complexity: O(m+n)
# Space complexity: O(1)
def backspaceCompare3(s1, s2):
    i = len(s1)-1 
    j = len(s2)-1

    while i >= 0 and j >= 0:
        skip1 = 0
        skip2 = 0

        while i >= 0:
            if s1[i] == '#':
                skip1 += 1
                i -= 1
            elif skip1 > 0:
                skip1 -= 1
                i -= 1
            else:
                break

        while j >= 0:
            if s2[j] == '#':
                skip2 += 1
                j -= 1
            elif skip2 > 0:
                skip2 -= 1
                j -= 1
            else:
                break

        if (i >= 0) != (j >= 0):
            return False

        if i >= 0 and j >= 0 and s1[i] != s2[j]:
            return False
        i -= 1
        j -= 1
        
    return True

print(backspaceCompare3(s1, s2))




