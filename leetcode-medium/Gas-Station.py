class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # base case
        if sum(cost) > sum(gas):
            return -1
        
        start, total = 0, 0
        
        for i in range(len(gas)):
            total += gas[i] - cost[i]

            # we can't begin/continue journey if fuel is insufficient, so restart from next station
            if total < 0:
                total = 0
                start = i + 1

        return start