class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        candidates = permutations(str(n))
        
        for cand in candidates:
            if cand[0] != '0' and bin(int("".join(cand))).count('1') == 1:
                return True
            
        return False
        