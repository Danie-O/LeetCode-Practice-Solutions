""" Using binary search"""
from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.time_map[key]
        l, r = 0, len(values) - 1

        while l <= r:
            mid = (l + r) // 2
            value, time = values[mid][0], values[mid][1]

            if time <= timestamp:
                res = value
                l = mid + 1
            else:
                r = mid - 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)