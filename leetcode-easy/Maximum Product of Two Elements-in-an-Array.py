"""Prompt: Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1)."""

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # USE TWO POINTERS TO FIND I AND J AND UPDATE MAX PRODUCT O(2N) = O(N)
        """
            Brute force: In first loop, find max index. Store value and the set to 0 in array.
            In second loop, find second max index. Then calculate: (max-1) * (second_max-1)
        """

        """In single iteration, find max and second max numbers, subtract 1 and then multiply them"""
        # TIME COMPLEXITY: O(n) ; SPACE COMPLEXITY: O(1)
        largest = 0
        second_largest = -1
        for i in range(len(nums)):
            if nums[i] >= largest:
                second_largest, largest = largest, nums[i]
            elif second_largest < nums[i]:
                second_largest = nums[i]
        return (largest - 1) * (second_largest - 1)
