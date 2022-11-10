class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # check for overflow
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        # check for negative
        negative = (dividend < 0) != (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                quotient += i
                i <<= 1
                temp <<= 1
        return -quotient if negative else quotient