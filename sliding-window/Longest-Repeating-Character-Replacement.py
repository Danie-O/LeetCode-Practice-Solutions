class Solution:
    # Time complexity: O(n), Space complexity: O(n) to store character counts
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        count = {}
        res = 0
        max_count = 0

        for end in range(len(s)):
            count[s[end]] = count.get(s[end],0) + 1
            max_count = max(max_count, count[s[end]])

            while (end - start + 1) - max_count > k:
                count[s[start]] -= 1
                start += 1
            res = max(res, (end - start + 1))
        return res




        