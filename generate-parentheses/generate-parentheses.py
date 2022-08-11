class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.generate([], n, n, res)
        return res
    
    def generate(self, prefix, left, right, res):
        if left == 0 and right == 0:
            res.append("".join(prefix))
        if left != 0:
            self.generate(prefix + ['('], left - 1, right, res)
        if left < right:
            self.generate(prefix + [')'], left, right - 1, res)