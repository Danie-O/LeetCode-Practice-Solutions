from typing import List

class Solution:
    # O(n) time => O(n) + O(n) + O(n) for the 3 iterations
    # O(2n) => O(n) space to store maximum from left & right

    # def trap(self, height: List[int]) -> int:
    #     result = 0
    #     left_maxs = [0] * len(height)
    #     right_maxs = [0] * len(height)

    #     curr_max = 0
    #     for i in range(1, len(height)):
    #         curr_max = max(curr_max, height[i - 1])
    #         left_maxs[i] = curr_max
            
    #     curr_max = 0
    #     for i in range(len(height) - 2, -1, -1):
    #         curr_max = max(curr_max, height[i + 1])
    #         right_maxs[i] = curr_max


    #     for i in range(len(height)):
    #         trapped_water = min(left_maxs[i], right_maxs[i]) - height[i]
    #         if trapped_water > 0:
    #             result += trapped_water
            
    #     return result
    

    # O(n) time complexity, because we go through entire array once
    # O(1) space, no auxiliary data structure was used (pointers and max trackers do not suffice)
    def trap(self, height: List[int]) -> int:
        result = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                result += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                result += right_max - height[right]
        return result


height = Solution()
print(height.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(height.trap([6,1,0,2,1,0,1,3,2,1,2,1]))