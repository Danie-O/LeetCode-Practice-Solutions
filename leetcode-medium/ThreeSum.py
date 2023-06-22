class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # SOLUTION 1 => TIME: , SPACE:
        # res = []
        # nums.sort()

        # for i, a in enumerate(nums):
        #     if i > 0 and a == nums[i-1]:
        #         continue
                
        #     l, r = i + 1, len(nums) - 1
        #     while l < r:
        #         current_sum =  a + nums[l] + nums[r]
        #         if current_sum > 0:
        #             r -= 1
        #         elif current_sum < 0:
        #             l += 1
        #         else:
        #             res.append([a, nums[l], nums[r]])
        #             l += 1
        #             while nums[l] == nums[l-1] and l < r:
        #                 l += 1
        # return res


        # SOLUTION 2 => TIME: , SPACE:
        # (Adapted)
        if len(nums) < 3:
            return []

        res = set()

        # 1. Split nums into three lists: negative numbers, positive numbers, and zeros
        n, p, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num)

        # 2. Create a separate set for negatives and positives for O(1) look-up times
        N, P = set(n), set(p)

        # 3. If there is at least 1 zero in the list, 
        # add all cases where -num exists in N  and num exists in P
        #   e.g (-3, 0, 3) = 0
        if z:
            for num in P:
                if -num in N:
                    res.add((-num, 0, num))

            # 3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
            if len(z) >= 3:
                res.add((0, 0, 0))

        # 4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
        #   exists in the positive number set
        from itertools import combinations

        for x, y in combinations(n, 2):
            target = -(x + y)
            if target in P:
                res.add(tuple(sorted([x, y, target])))

        # 5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
        #   exists in the negative number set

        for x, y in combinations(p, 2):
            target = -(x + y)
            if target in N:
                res.add(tuple(sorted([x, y, target])))

        return [list(x) for x in res]

