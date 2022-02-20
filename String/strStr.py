"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

https://leetcode.com/problems/implement-strstr/discuss/1774271/Python-Sliding-window
"""


def strStr(haystack, needle):
    if (needle == ""):
        return 0
    if (needle not in haystack):
        return -1
    return len(haystack.split(needle)[0])    



print(strStr("hello", "ll"))
print(strStr("", ""))
print(strStr("aaaaaa","bba"))