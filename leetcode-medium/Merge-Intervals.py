class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
                - define result array - define new_interval = intervals[0]
                - for each interval in input, 
                  check if 'new interval' and the current interval are overlapping
                - if overlapping, merge and update new interval
                - if not overlapping, append new interval to result, and update new interval
            """
        res = []
        intervals.sort()
        new_interval = intervals[0]

        # base case
        if len(intervals) == 1: return intervals

        for i in range(1, len(intervals)):
            if intervals[i][0] > new_interval[1]:  
                # no overlapping
                res.append(new_interval)
                new_interval = intervals[i]
            else: 
                # there is overlapping, so we need to merge
                new_interval = [
                    min(new_interval[0], intervals[i][0]),
                    max(new_interval[1], intervals[i][1])
                ]
                
        # incase we merge all intervals, we'll need to append it to the result
        res.append(new_interval)
        return res




