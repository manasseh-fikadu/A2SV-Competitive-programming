class Solution:
    def calculate(self, s: str) -> int:
        output, curr, sign, stack = 0, 0, 1, []
        
        for char in s:
            if char.isdigit():
                curr = curr * 10 + int(char)
            elif char in "+-":
                output += (curr * sign)
                curr = 0                
                if char == '-':
                    sign = -1
                else:
                    sign = 1
            elif char == '(':
                stack.append(output)
                stack.append(sign)
                output = 0
                sign = 1
            elif char == ')':
                output += (curr * sign)
                output *= stack.pop()
                output += stack.pop()
                curr = 0
                
        return output + (curr * sign)
