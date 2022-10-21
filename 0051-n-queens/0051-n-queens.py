class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.result = []
        self.dfs([],[],[])
        ans = []
        for sol in self.result:
            board = []
            for i in sol:
                board.append('.'*i + 'Q' + '.'*(n-i-1))
            ans.append(board)
            
        return ans
    
    def dfs(self, queens, xy_dif, xy_sum):
            p = len(queens)
            if p == self.n:
                self.result.append(queens)
                return None
            for q in range(self.n):
                if q not in queens and p-q not in xy_dif and p+q not in xy_sum:
                    self.dfs(queens+[q], xy_dif+[p-q], xy_sum+[p+q])