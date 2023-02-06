class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        count = 0
        for x2, y2 in self.points:
            if x1 == x2 or y1 == y2 or abs(x1 - x2) != abs(y1 - y2):
                continue
            if (x1, y2) in self.points and (x2, y1) in self.points:
                count += self.points[(x1, y2)] * self.points[(x2, y1)] * self.points[(x2, y2)]
        return count
                
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)