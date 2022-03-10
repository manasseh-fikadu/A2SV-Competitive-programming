class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])
        
        def dfs(row, col):
            if row<0 or col<0 or row>=n or col>=m or board[row][col]!="O":
                return 
            board[row][col]="I"
            dfs(row+1,col)
            dfs(row-1,col)
            dfs(row,col+1)
            dfs(row,col-1)
                    
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0 or i == n-1 or j == m-1:
                    if board[i][j] == "O":
                        dfs(i,j)
        for i in range(n):
            for j in range(m):
                if 0 < i < n-1 and 0 < j < m-1 and board[i][j] == "O": 
                    board[i][j] = "X"
                if board[i][j] == "I":    
                    board[i][j] = "O"

                    
                    