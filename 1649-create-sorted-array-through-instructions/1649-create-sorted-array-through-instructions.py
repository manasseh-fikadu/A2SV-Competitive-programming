class BinaryIndexedTree:
    def __init__(self, n: int):
        self.tree = [0] * (n + 1)

    def update(self, i: int, delta: int):
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i)

    def query(self, i: int) -> int:
        count = 0
        while i > 0:
            count += self.tree[i]
            i -= i & (-i)
        return count    

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        BIT_MAX = 10 ** 5 + 1
        MODULO = 10 ** 9 + 7
        bit = BinaryIndexedTree(BIT_MAX)
        cost = 0
        for i, x in enumerate(instructions):
            less_than = bit.query(x - 1)
            greater_than = i - bit.query(x)
            cost += min(less_than, greater_than)
            bit.update(x, 1)
        return cost % MODULO
        