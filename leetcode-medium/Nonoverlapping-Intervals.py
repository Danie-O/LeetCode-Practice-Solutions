class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
            - sort intervals
            - initialise prev
            - "" removed_count = 0
            - return 0 if base case is true
            - else, for every interval in input;
            - if prev[1] > curr[0]:
                removed_count += 1
            - return removed_count
        """
        # base case
        if len(intervals) <= 1:
            return 0 

        intervals.sort(key=lambda x: (x[1]))
        prev = intervals[0][1]
        removed_count = 0

        for curr in range(len(intervals) - 1):
            if prev > intervals[curr + 1][0]: 
                # overlapping occurs, so remove the curr interval by updating removed_count
                removed_count += 1
            else:
                # no overlapping
                prev = intervals[curr + 1][1]
        
        return removed_count

