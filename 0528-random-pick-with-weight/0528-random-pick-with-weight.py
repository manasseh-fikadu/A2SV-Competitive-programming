class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.sum = sum(w)
        self.len = len(w)
        self.probability = [i / self.sum for i in w]

    def pickIndex(self) -> int:
        return random.choices(range(self.len), weights=self.probability)[0]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()