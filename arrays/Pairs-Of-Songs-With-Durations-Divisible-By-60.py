class Solution:
    # Time complexity: O(n), Space complexity: O(1)
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        rem_count = [0] * 60
        count = 0

        for duration in time:
            rem = duration % 60

            # check if other exact multiples of 60 exist, to form pair
            if not rem:
                count += rem_count[0]
            else:
                count += rem_count[60 - rem]
            rem_count[rem] += 1

        return count

        