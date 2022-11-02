class Solution:
    def findComplement(self, num: int) -> int:
        bits = int(math.log(num, 2)) + 1
        mask = (1 << bits) - 1
        print(mask)
        return num ^ mask