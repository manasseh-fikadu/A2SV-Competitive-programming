class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        stack = []
        num = 0
        op = '+'
        all_ops = {'+', '-', '*', '/'}
        nums = set(str(x) for x in range(10))
        
        for i in range(len(s)):
            char = s[i]
            if char in nums:
                num = num * 10 + int(char)
            if char in all_ops or i == len(s) -1:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack[-1] *= num
                elif op == '/':
                    stack[-1] /= num
                    stack[-1] = math.trunc(stack[-1])
                num = 0
                op = char
        return sum(stack)
