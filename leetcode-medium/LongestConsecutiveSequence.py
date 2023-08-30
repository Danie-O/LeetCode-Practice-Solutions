class Solution:
    # Time: O(3n) => O(n)
    # Space: O(n), used while creating set
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)     # O(n) to create set from input
        longest_length = 0

        for num in nums: # O(n) to check for start of sequence
            if (num - 1) not in hashset:
                current_length = 0
                # O(n) to count length of sequences
                while (num + current_length) in hashset:
                    current_length += 1
                longest_length = max(current_length, longest_length) 

        return longest_length

            