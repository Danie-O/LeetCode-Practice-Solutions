from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # USE TWO POINTERS TO FIND I AND J AND UPDATE MAX PRODUCT O(2N) = O(N)
        """
            In first loop, find max index. Store value and the set to 0 in array.
            In second loop, find second max index. Then calculate: (max-1) * (second_max-1)
        """

        """In single iteration, find max and second max numbers, subtract 1 and then multiply them"""