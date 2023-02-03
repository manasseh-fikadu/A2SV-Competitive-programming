class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.s = sum(w)
        self.l = len(w)
        self.p = [i / self.s for i in w]

    def pickIndex(self) -> int:
        return random.choices(range(self.l), weights=self.p)[0]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()