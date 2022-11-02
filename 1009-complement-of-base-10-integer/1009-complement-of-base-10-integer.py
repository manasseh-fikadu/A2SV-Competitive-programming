class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        if N == 1:
            return 0
        bits = int(math.log(N, 2)) + 1

        mask = (1 << bits) - 1

        return N ^ mask