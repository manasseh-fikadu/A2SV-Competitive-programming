class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        #DFS
        dx = [-1, -1, -1, 0, 1, 1, 1, 0] 
        dy = [-1, 0, 1, 1, 1, 0, -1, -1]

        m = len(board)
        n = len(board[0])

        def in_board(x, y):
            return 0 <= x < m and 0 <= y < n

        def dfs(x, y):
            count = 0
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if in_board(nx, ny) and board[nx][ny] == 'M':
                    count += 1
            if count > 0:
                board[x][y] = str(count)
                return
            board[x][y] = 'B'
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if in_board(nx, ny) and board[nx][ny] == 'E':
                    dfs(nx, ny)

        x, y = click
        if board[x][y] == 'M':
            board[x][y] = 'X'
        else:
            dfs(x, y)

        return board
                        
                    
        