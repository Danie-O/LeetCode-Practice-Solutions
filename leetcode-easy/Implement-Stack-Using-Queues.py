from collections import deque

""" PROMPT:

Implement a last-in-first-out (LIFO) stack using only two queues. 
The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, 
which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. 
You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.

"""

class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        if not self.empty():
            # pop and push all elements except last element(the element to be popped)
            for i in range(len(self.q) - 1):
                self.push(self.q.popleft())
            # now, pop the leftmost element which was formerly rightmost
            return self.q.popleft()

    def top(self) -> int:
        if not self.empty():
            return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
x = 9
obj = MyStack()
obj.push(x)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()
print(param_2)
print(param_3)
print(param_4)

# Example 2
# myStack = MyStack()
# myStack.push(1)
# myStack.push(2)
# myStack.top() # return 2
# myStack.pop() # return 2
# myStack.empty() # return False