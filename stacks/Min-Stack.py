                
class MinStack:

    def __init__(self):
        self.stack = []
        self.current_min = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.current_min or val <= self.current_min[-1]:
            self.current_min.append(val)
        

    def pop(self) -> None:
        if self.stack:
            if self.stack[-1] == self.current_min[-1]:
                self.current_min.pop()
            self.stack.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        

    def getMin(self) -> int:
        if self.current_min:
            return self.current_min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()