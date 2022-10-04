class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        
        for i in range(n + 1):
            bi = str(bin(i))[2:]
            for j in range(len(bi)):
                if bi[j] == "1":
                    res[i] += 1
                    
        return res