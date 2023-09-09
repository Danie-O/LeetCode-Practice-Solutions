class Solution:
    def maxSubstringLength(self, s: str):
        maxLength = 0
        seen = set()
        left = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[right])
                # shrink window due to repeating character
                left += 1
            seen.add(s[right])
            maxLength = max(maxLength, (right - left) + 1)

        return maxLength

sample = Solution()
print(f"Expected: 1, Actual: {sample.maxSubstringLength('bbbbb')}")

print(f"Expected: 1, Actual: {sample.maxSubstringLength('abcabcbb')}")