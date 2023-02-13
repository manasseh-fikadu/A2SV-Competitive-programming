class Node:
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.val = val
        self.set = set()

class AllOne:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}

    def add(self, node, key):
        if node.val + 1 != node.next.val:
            new = Node(node.val + 1)
            new.next = node.next
            new.prev = node
            new.prev.next = new
            new.next.prev = new
        else:
            new = node.next

        new.set.add(key)
        return new

    def addPrev(self, node, key):
        if node.val - 1 != node.prev.val:
            new = Node(node.val - 1)
            new.next = node
            new.prev = node.prev
            new.prev.next = new
            new.next.prev = new
        else:
            new = node.prev

        new.set.add(key)
        return new

    def inc(self, key) -> None:
        if key in self.map:
            node = self.map[key]
            self.map[key] = self.add(node, key)
            node.set.remove(key)
            if not node.set:
                node.prev.next = node.next
                node.next.prev = node.prev
                node.prev = None
                node.next = None
        else:
            self.map[key] = self.add(self.head, key)

    def dec(self, key) -> None:
        if key in self.map:
            node = self.map[key]
            node.set.remove(key)
            del self.map[key]
            if node.val > 1:
                self.map[key] = self.addPrev(node, key)
            if not node.set:
                node.prev.next = node.next
                node.next.prev = node.prev
                node.prev = None
                node.next = None

    def getMaxKey(self) -> str:
        if not self.tail.prev.set:
            return ""
        answer = self.tail.prev.set.pop()
        self.tail.prev.set.add(answer)
        return answer

    def getMinKey(self) -> str:
        if not self.head.next.set:
            return ""
        answer = self.head.next.set.pop()
        self.head.next.set.add(answer)
        return answer
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()