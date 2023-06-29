class Solution:

    # TIME: O(nlogn): to retrieve elements from the heap    ; 
    # SPACE: O(n) due to extra space for heap
    def lastStoneWeight(self, stones: List[int]) -> int:
        # use a min heap to simulate a max heap
        # for each res > 0, push it back to the heap to avoid repeated sorting
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            max1 = heapq.heappop(stones)
            max2 = heapq.heappop(stones)

            # due to negating elements, max2 should be >= max1
            if max2 > max1:
                heapq.heappush(stones, max1 - max2)
        
        return abs(stones[0]) if stones else 0


    # TIME: O(n * nlogn) ; SPACE: O(1)
    # def lastStoneWeight(self, stones: List[int]) -> int:
    #     while len(stones) > 1:
    #         stones.sort()  # Sort the stones in ascending order
    #         y = stones.pop()  # Take the heaviest stone
    #         x = stones.pop()  # Take the second heaviest stone
    #         res = y - x  # Calculate the difference

    #         if res > 0:
    #             stones.append(res)  # Add the remaining stone back to the list

    #     return stones[0] if stones else 0
