class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]
        else:
            positives = [i for i in range(1, n//2 + 1)] 
            negatives = [-i for i in range(1, n//2 + 1)] 
            zeroes = [0] * (n % 2)
            
            return positives + negatives + zeroes