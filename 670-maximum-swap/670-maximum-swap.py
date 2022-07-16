class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        for i in range(len(digits)):
            _max = i
            for j in range(i + 1, len(digits)):
                if digits[j] >= digits[_max] and digits[j] != digits[i]:
                    _max = j
                if j == len(digits) - 1 and _max != i:    
                    digits[i], digits[_max] = digits[_max], digits[i]
                    return int(''.join(digits))
        return int(''.join(digits))
            