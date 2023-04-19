""" PROMPT: Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # USING HASHMAPS
        mapST, mapTS = {}, {}

        for c1, c2 in zip(s, t):
            if (c1 in mapST and mapST[c1] != c2) or (c2 in mapTS and mapTS[c2] != c1):
                #  we check both hashmaps since; "no two characters may map to the same character"
                return False
            mapST[c1] = c2
            mapTS[c2] = c1

        return True


# Examples
example = Solution()

# Example 1:
s = "egg"
t = "add"
print(example.isIsomorphic(s, t))
# Output: true
# Explanation: e -> a (correct); g -> d (correct)

# Example 2:
s = "foo"
t = "bar"
print(example.isIsomorphic(s, t))
# Output: false
# Explanation: f -> b (correct); o -> a and r (incorrect)
