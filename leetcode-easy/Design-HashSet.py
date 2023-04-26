class MyHashSet:
    def __init__(self):
        self.size = 10000
        self.set = [None] * self.size

    # helper function for hashing keys
    def hash_key(self, key: int) -> int:
        return key % self.size

    def add(self, key: int) -> None:
        hash_val = self.hash_key(key)

        if self.set[hash_val]:
            self.set[hash_val].append(key)
        else:
            self.set[hash_val] = [key]

    def remove(self, key: int) -> None:
        hash_val = self.hash_key(key)

        if self.set[hash_val]:
            while key in self.set[hash_val]:
                self.set[hash_val].remove(key)

    def contains(self, key: int) -> bool:
        hash_val = self.hash_key(key)

        if self.set[hash_val]:
            return key in self.set[hash_val]
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
