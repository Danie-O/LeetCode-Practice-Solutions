import collections

""" QUESTION:
    Design a HitCounter class. In this class, there are the following functions:

    HitCounter(): No-argument constructor
    void hit(int timestamp): Indicates that a tap occurs at the specified time
    int getHits(int timestamp): Returns the total number of hits within 300 seconds before the specified time
    Where timestamp is in seconds.
"""
# USING A QUEUE
class HitCounter:
    def __init__(self):
        self.queue = collections.deque()

    def hit(self, timestamp):
        self.queue.append(timestamp)
    
    def getHit(self, timestamp):
        """ go through queue and remove any timestamp that falls is not within 5 min range of input timestamp"""
        while self.queue and (timestamp - self.queue[0] >= 300):
            self.queue.popleft()
        
        # when we have removed all out of range timestamps
        return len(self.queue)


# USING TWO ARRAYS TO STORE TIMESTAMPS & NO OF HITS BY HASHING HIT TIMESTAMPS
class HitCounter:
    def __init__(self):
        self.timestamps = [] * 300
        self.hits = [0] * 300

    def hit(self, timestamp):
        ...
        index = timestamp % 300
        # if we havent hit timestamp before or if most recent hit to that index is a different timestamp
        # , reset number of hits and assign set timestamp to most recent hit
        if self.timestamps[index] != timestamp:
            self.timestamps[index] = timestamp
            self.hits[index] = 1
        else:
            # multiple hits were made at the same time, so just increment hit count
            self.hits[index] += 1
    
    def getHit(self, timestamp):
        res = 0
        for i in range(300):
            if timestamp - self.timestamps[i] < 300:
                res += self.hits[i]

        return res