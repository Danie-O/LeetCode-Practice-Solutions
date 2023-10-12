class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # sort by cost to city A, so first n of 2n costs are min cost to reach dest A
        sorted_costs = sorted(costs, key= lambda x: x[0] - x[1])
        min_cost = 0

        # get costs to travel to city A(for first half(n) people)
        for i in range(len(costs) // 2):
            min_cost += sorted_costs[i][0]
        
        # get remaining costs which are minimum to travel to city B
        for i in range(len(costs) // 2, len(costs)):
            min_cost += sorted_costs[i][1]
        
        return min_cost
        