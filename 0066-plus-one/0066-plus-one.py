class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)):
            digits[i] = str(digits[i])
            
        return list(str(int("".join(digits)) + 1))