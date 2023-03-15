def isPalindrome(self, s):
    l, r = 0, len(s)-1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l <r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l +=1; r -= 1
    return True

def isPalindrome(self, s: str) -> bool:
        
        convert = ''.join(filter(str.isalnum, s))
        lower = convert.lower()
        print(lower)
        
        # Check for empty string
        if not s:
            return True

        size = len(lower)-1
        middle = len(lower)//2
        print(middle)
        
        for i in range(middle):
            if (lower[i] != lower[size-i]):
                return False
        
        return True