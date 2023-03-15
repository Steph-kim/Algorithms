"""
Substring Removal

Given a string seq consisting of the characters 'A' and 'B' only, in one move, yuou can delete either an "AB" or a "BB" substring.
After a move, the remaining parts of the string get concatenated.

Find the minimum possible length of the remaining string after performing any number of moves.

Note: A substring is a contiguous sequence of string.

Example
seq = "BABBA"

Using 0-based indexingm the following moves are optimal.

    - Delete the substring "AB" starting at index 1. 
      "BABBA" -> "BBA"
    - Delete the substring "BB" starting at index 0.
      "BBA"   -> "A"

There are no more moves so the minimum possible length of the remaining string is 1.

"""

# if we are at 'B', we want the top element of the stack to be 'A' or 'B'
#     if it is 'A' or 'B', add to the stack
#     otherwise, add to the stack
# if we are at 'A', we add to the stack

def getMinLength(seq):
    stack = []
    for char in seq:
        if char == 'B':
            if stack:
                stack.pop()
            else: 
                stack.append(char)
        else:
            stack.append(char)
    return len(stack)
        
    
seq = "ABAAABBB"


print(getMinLength(seq))