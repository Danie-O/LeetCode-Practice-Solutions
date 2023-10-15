class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:
    def __init__(self, homepage: str):
        self.curr = ListNode(homepage)

    def visit(self, url: str) -> None:
        self.curr.next = ListNode(url, prev=self.curr)
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        # keep going back in history until we reach start of history or no of steps
        while self.curr.prev and steps:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.val

    def forward(self, steps: int) -> str:
        # keep going forward in history until we reach end of history or no of steps
        while self.curr.next and steps:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)