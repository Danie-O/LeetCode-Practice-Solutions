class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.stream = [0] * self.n
        self.ptr = 0
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey - 1] = value
        increasing_stream = []

        if self.ptr == idKey - 1:

            while self.ptr < len(self.stream) and self.stream[self.ptr] != 0:
                increasing_stream.append(self.stream[self.ptr])
                self.ptr += 1
            return increasing_stream
        else:
            return increasing_stream
        


# The OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)