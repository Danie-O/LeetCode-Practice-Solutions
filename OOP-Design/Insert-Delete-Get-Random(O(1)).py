import random

class RandomizedSet:

    def __init__(self):
        self.lst = []    # O(1) time to add at and remove from end of a list
        self.map = defaultdict(int) # maps values to their indices in self.lst
        self.size = 0   # tracks size of self.lst to enable us map values to indices

    def insert(self, val: int) -> bool:
        if val in self.map: return False

        self.lst.append(val)
        self.map[val] = self.size
        self.size += 1

        return True


    def remove(self, val: int) -> bool:
        if val not in self.map: return False

        # Override place of val with last element in self.lst
        val_index, last_element = self.map[val], self.lst[-1]

        self.lst[val_index], self.map[last_element] = last_element, val_index

        self.lst.pop()
        del self.map[val]
        self.size -= 1
        return True


    def getRandom(self) -> int:
        return random.choice(self.lst)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()