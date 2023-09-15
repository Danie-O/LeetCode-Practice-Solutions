""" REVISIT!! 

    Given two strings s and t of lengths m and n respectively, return the minimum window substring
    of s such that every character in t (including duplicates) is included in the window. 
    If there is no such substring, return the empty string "".
    The testcases will be generated such that the answer is unique.

    Example 1:

    Input: s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"
    Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t) > len(s): return ""

        countT, window = {}, {}
        for ch in t:
            countT[ch] = 1 + countT.get(ch, 0)

        have, need = 0, len(countT)
        res = [-1, -1]
        resLength = float("inf")

        l = 0
        for r in range(len(s)):
            ch = s[r]
            window[ch] = 1 + window.get(ch, 0)

            if ch in countT and window[ch] == countT[ch]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLength:
                    res = [l, r]
                    resLength = (r - l + 1)
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
            
        l, r = res
        return s[l : r + 1] if resLength != float("inf") else ""

        