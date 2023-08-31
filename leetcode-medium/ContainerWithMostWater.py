class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Bruteforce Approach (O(n^2) time)
        # res = 0
        #
        # for l in range(len(height)):
        #     for r in range(l + 1, len(height)):
        #         area = (r - l) * min(height[l], height[r])
        #         res = max(res, area)
        # return res


        # 2 pointer approach (LINEAR TIME SOLUTION)
        max_area = 0
        l, r = 0, len(height) - 1

        while l < r:
            current_area =  (r - l) * min(height[l], height[r])
            max_area = max(max_area, current_area)

            # update ptrs based on possible height increase or decrease
            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                l += 1
        
        return max_area
