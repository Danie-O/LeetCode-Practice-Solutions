""" PROMPT:
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.
    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

#solution 1
# from collections import Counter

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
        
#         return Counter(s) == Counter(t)



#solution 2
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s = sorted(s)
        t = sorted(t)
        return s == t


# Examples
example = Solution()

# Example 1:
s = "anagram"
t = "nagaram"

print(example.isAnagram(s, t))
# Output: true

# Example 2:
s2 = "rat"
t2 = "car"

print(example.isAnagram(s2, t2))
# Output: false