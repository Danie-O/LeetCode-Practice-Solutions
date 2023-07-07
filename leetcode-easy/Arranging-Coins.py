class Solution:
    def arrangeCoins(self, n: int) -> int:
        # with O(n) time
        # count = 0
        # i = 1
        # while n >= i:
        #     n -= i
        #     count += 1
        #     i += 1
        # return count 

        # using binary search => O(log n)
        l, r = 1, n

        while l <= r:
            mid = (l + r) // 2
            coins = (mid / 2) * (mid + 1)
            if coins == n:
                return mid
            elif coins < n:
                l = mid + 1
            else:
                r = mid - 1
        return r

        # O(1) solution
        # return sqrt(2 * n + 0.25) - 0.5

