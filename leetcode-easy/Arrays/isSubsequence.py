class Solution:
    # Time complexity: O(t), where t = length of main string
    # Space complexity: O(1) because no extra data structure is created
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
            
        index = 0

        for char in t:
            if index < len(s) and char == s[index]:
                index += 1
        return index == len(s)
        