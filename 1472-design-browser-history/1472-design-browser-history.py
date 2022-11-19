class Node:
    
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = Node(homepage)
        self.head = self.current
        self.tail = self.current

    def visit(self, url: str) -> None:
        self.current.next = Node(url)
        self.current.next.prev = self.current
        self.current = self.current.next
        self.tail = self.current

    def back(self, steps: int) -> str:
        while steps and self.current.prev:
            self.current = self.current.prev
            steps -= 1
        return self.current.val

    def forward(self, steps: int) -> str:
        while steps and self.current.next:
            self.current = self.current.next
            steps -= 1
        return self.current.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)