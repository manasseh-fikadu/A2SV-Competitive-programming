class RandomizedCollection:
    def __init__(self):
        self.d = defaultdict(set)
        self.nums = []


    def insert(self, val: int) -> bool:
        self.d[val].add(len(self.nums))
        self.nums.append(val)
        return len(self.d[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.d[val]:
            return False
        idx, last = self.d[val].pop(), self.nums[-1]
        self.nums[idx] = last
        self.d[last].add(idx)
        self.d[last].discard(len(self.nums) - 1)
        self.nums.pop()
        return True

    def getRandom(self) -> int:
        randVal = random.randint(0, len(self.nums) - 1)
        return self.nums[randVal]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()