class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        self.dfs(s, 0, res)
        return res

    def dfs(self, s, index, res):
        if index == len(s):
            res.append(s)
            return
        if s[index].isalpha():
            self.dfs(s[:index] + s[index].upper() + s[index+1:], index+1, res)
            self.dfs(s[:index] + s[index].lower() + s[index+1:], index+1, res)
        else:
            self.dfs(s, index+1, res)