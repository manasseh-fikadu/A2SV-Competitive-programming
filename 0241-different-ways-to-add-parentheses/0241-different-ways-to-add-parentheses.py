class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]
        
        res = []
        for i, char in enumerate(expression):
            if char in ['+', '-', '*']:
                left_res = self.diffWaysToCompute(expression[:i])
                right_res = self.diffWaysToCompute(expression[i+1:])
                
                for left in left_res:
                    for right in right_res:
                        if char == '+':
                            res.append(left + right)
                        elif char == '-':
                            res.append(left - right)
                        elif char == '*':
                            res.append(left * right)
        return res