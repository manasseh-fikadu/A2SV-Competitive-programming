class Solution:
    def maximum69Number (self, num: int) -> int:
        _max = num
        num = list(str(num))
        for i, d in enumerate(num):
            if d == '6':
                num[i] = '9'
                curr = int(''.join(num))
                _max = max(_max, curr)
                num[i] = '6'
                
        return _max
                