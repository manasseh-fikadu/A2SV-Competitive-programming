class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.ptr = 1
        self.stream = [None] * (n + 1)

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value
        if idKey == self.ptr:
            res = []
            while self.ptr <= self.n and self.stream[self.ptr]:
                res.append(self.stream[self.ptr])
                self.ptr += 1
            return res 
        
        return []
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)