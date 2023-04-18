from collections import Counter

""" Prompt: Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1. """


class Solution:
    def firstUniqChar(self, s: str) -> int:
        # create counter of unique characters and their count
        counter = Counter(s)

        for i in range(len(s)):
            if counter[s[i]] == 1:
                # if count of element is 1, it's unique
                return i    # return its index

        return -1   # return -1, if there is no unique character in input string


""" Note:
    I saw a solution which uses s.rindex and index to determine if the last seen occurrence of the character is the same as its first occurence. 
    Interesting  way of looking at this question in my opinion.
    See solution below:

    def firstUniqChar(self, s: str) -> int:
        for i in s:
            if s.rindex(i) == s.index(i):
                return s.index(i)            
        return -1
"""


# Examples
example = Solution()

# Example 1:
s = "Leetcode"
print(example.firstUniqChar(s))
# Output: 0
# Explanation: L is the first unique element in the string
