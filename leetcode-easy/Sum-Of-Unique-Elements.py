from typing import List

""" PROMPT:

    You are given an integer array nums. 
    The unique elements of an array are the elements that appear exactly once in the array. Return the sum of all the unique elements of nums.
"""

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        # Using hashmap only
        seen = {} # key= number: value= number of times seen
        total = 0 

        for i in range(len(nums)):
            if nums[i] not in seen: # if we havent seen the number before
                total += nums[i] # add to total
                seen[nums[i]] = 1 # now we've seen nums[i], assign the value of nums[i] to 1
            else:
                while seen.get(nums[i]): 
                    # if seen before, subtract number from total and decrement value in 'seen' hashmap
                    total -= nums[i]
                    seen[nums[i]] -= 1
        return total


        # Using set and hashmap
        # frequency = {}
        # for num in nums:
        #     if num in frequency:
        #         frequency[num] += 1
        #     else:
        #         frequency[num] = 1
        
        # # Create a set to store the unique elements
        # unique_elements = set()
        # for num, freq in frequency.items():
        #     if freq == 1:
        #         unique_elements.add(num)
        
        # return sum(unique_elements)



# Examples
example = Solution()

# Example 1:
nums = [1,2,3,2]
print(example.sumOfUnique(nums))
# Output: 4
# Explanation: The unique elements are [1,3], and the sum is 4.


# Example 2:
nums2 = [1,1,1,1,1]
print(example.sumOfUnique(nums2))
# Output: 0
# Explanation: There are no unique elements, and the sum is 0.