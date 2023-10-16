class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals):
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        s, e = 0, 0
        res, count = 0, 0
        # iterate through both arrays and increment count if there is a new interval(start),
        #  while current meeting is still ongoing (start < end)
        while s < len(start):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1  # when a meeting ends, we reduce the number of meeting rooms needed
            res = max(res, count)
        return res