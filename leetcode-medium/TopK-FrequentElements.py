from collections import Counter
from typing import List
from heapq import heapify, heappop


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # APPROACH 1: Using bucket sort

        # O(n) time, 
        # O(n) space {for creating bucket, frequencies hashmap and result array}
        # frequencies = {}
        # bucket = [[] for i in range(len(nums) + 1)]

        # for num in nums:
        #     frequencies[num] = 1 + frequencies.get(num, 0)
        
        # for val, freq in frequencies.items():
        #     bucket[freq].append(val)
        
        # res = []
        # for i in range(len(bucket) - 1, 0, -1):
        #     for val in bucket[i]:
        #         res.append(val)
        #         if len(res) == k:
        #             return res
                


        # APPROACH 2: Using Counter to build frequency map

        # count_map = Counter(nums)
        # counts = count_map.most_common(k)
        # return [item[0] for item in counts] 
        #we can also use the ff. to get counts: 
        # sorted(count_map.items(), key=lambda pair: pair[1], reverse=True)
        
        

        # APPROACH 3: Using maxHeap
        # Build hashmap of top k frequent elements and convert it into an output array
        # Heapify array of (freq, num) tuples, then, pop from maxHeap k times
        # O(N log k) time for popping from maxHeap k times
        frequencies = {}
        for num in nums:
            frequencies[num] = 1 + frequencies.get(num, 0)

        # build max heap using frequencies as key => max frequency would be min element in heap
        maxHeap = [(-frequency, num) for num, frequency in frequencies.items()]
        heapify(maxHeap)

        res = []
        for i in range(k):
            res.append(heappop(maxHeap)[1])
        
        return res




# Testing
nums = Solution()
print(nums.topKFrequent([1,1,1,4,9,9,9,9,9,0,9], 2))

