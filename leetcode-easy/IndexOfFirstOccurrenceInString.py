"""PROMPT:
    Given two strings needle and haystack, 
    return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = 0
        r = 0
        len_haystack = len(haystack)
        len_needle = len(needle)

        if needle == haystack:
            return 0

        while l <= (len_haystack - len_needle):
            r = 0
            while r < len_needle and haystack[l+r] == needle[r]:
                r += 1
            if r == len_needle:
                return l
            l += 1
        return -1
    

# Examples
s = Solution()

# Example 1:
haystack = "sadbutsad"
needle = "sad"
print(s.strStr(haystack, needle))
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.


# Example 2:
haystack2 = "leetcode"
needle2 = "leeto"
print(s.strStr(haystack2, needle2))
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.