class Solution:
    def isValid(self, s: str) -> bool:
        paren = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []

        for c in s:
            if c not in paren:
                stack.append(c)
                continue
            if not stack or stack[-1] != paren[c]:
                return False
            stack.pop()
            
        return not stack