""" QUESTION:
    Design a queue-like data structure that moves the most recently used elements to the end of the queue.

    Implement the MRUQueue class:
    - MRUQueue(int n): initialize the queue by [1,2,3,.... ,n] Construct MRUQueue.
    - fetch(int k): return the kth element in the queue (indexed from 1) and move it to the end of the queue
"""
from sortedcontainers import SortedList


class MRUQueue:
    def __init__(self, n: int):
        # [(priority value, actual value)]
        self.q = SortedList((i, i) for i in range(1, n + 1))

    def fetch(self, k: int) -> int:
        _, num = self.q.pop(k - 1)
        if self.q:
            maxPriority = self.q[-1][0]
            self.q.add((maxPriority + 1, num))
        else:
            self.q.add((0, num))
        return num
