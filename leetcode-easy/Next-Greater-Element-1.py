from typing import List
""" PROMPT:

The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
"""
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in range(len(nums1)):
            nxt = nums2.index(nums1[i]) + 1    # find index of next element

            while nxt < len(nums2):    # while index of next element in nums2 is not out of bounds,
                if nums2[nxt] > nums1[i]:
                    res.append(nums2[nxt])    # append to result list if the next element is greater
                    break
                nxt += 1    # if not, move to next element in nums2 list
            if len(res) < i+1:    # if at end of nums2 and no greater element was found, answer= -1
                res.append(-1)
        return res


# Examples
example = Solution()

# Example 1:
# Input: 
nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(example.nextGreaterElement(nums1=nums1, nums2=nums2))
# Output: 
# [-1,3,-1]

# Explanation: The next greater element for each value of nums1 is as follows:
# - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
# - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
# - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.