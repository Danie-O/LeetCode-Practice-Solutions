<<<<<<< HEAD
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # # Searching is faster using hashset --> O(1).
        # [O(N)time, O(M) space -- where len(stones) = N and len(jewels) = M]

        jewel_count = 0
        jewels_set = set(jewels)

        for s in stones:
            if s in jewels_set:
                jewel_count += 1
        return jewel_count


# Examples
example = Solution()

# Example 1:
jewels = "aA"
stones = "aAAbbbb"
print(example.numJewelsInStones(jewels, stones))
# Output: 3
# Explanation: jewels in stones: "a", "A", "A"

# Example 2:
jewels = "z"
stones = "ZZ"
print(example.numJewelsInStones(jewels, stones))
# Output: 0
# Explanation: jewels in stones: 0
=======
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # # Searching is faster using hashset --> O(1).
        # [O(N)time, O(M) space -- where len(stones) = N and len(jewels) = M]

        jewel_count = 0
        jewels_set = set(jewels)

        for s in stones:
            if s in jewels_set:
                jewel_count += 1
        return jewel_count


# Examples
example = Solution()

# Example 1:
jewels = "aA"
stones = "aAAbbbb"
print(example.numJewelsInStones(jewels, stones))
# Output: 3
# Explanation: jewels in stones: "a", "A", "A"

# Example 2:
jewels = "z"
stones = "ZZ"
print(example.numJewelsInStones(jewels, stones))
# Output: 0
# Explanation: jewels in stones: 0
>>>>>>> f996e72cb1d329be37dbbd0c7de705eafc1a58a0
