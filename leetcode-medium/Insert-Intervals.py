class Solution:
    # TIME: O(N) => we go through entire array of intervals at most once(N times)
    # SPACE: O(N) => we create new result array that would store all input intervals if there are 1 or no merges
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # base case: new interval lies at the beginning of input intervals array
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                # merge new interval with overlapping interval
                newInterval = [ 
                    min(newInterval[0], intervals[i][0]), 
                    max(newInterval[1], intervals[i][1])          
                ]
        
        # if all intervals are merged, or if the new interval falls at the end of input intervals array
        res.append(newInterval)

        return res


