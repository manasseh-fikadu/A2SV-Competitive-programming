class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)
        
        def collector(board):
            
            for row in range(9):
                for col in range(9):
                    if board[row][col] != '.':
                        cols[col].add(board[row][col])
                        rows[row].add(board[row][col])
                        squares[(row // 3, col // 3)].add(board[row][col])
        
        collector(board)
        
        
        def isValidSudoku(board):
            iscols = defaultdict(set)
            isrows = defaultdict(set)
            issquares = defaultdict(set)

            for r in range(9):
                for c in range(9):
                    if (board[r][c] in isrows[r] or board[r][c] in iscols[c] or board[r][c] in issquares[(r // 3, c // 3)]):
                        return False

                    iscols[c].add(board[r][c])
                    isrows[r].add(board[r][c])
                    issquares[(r // 3, c // 3)].add(board[r][c])
            
            return True
        
        def backtrack(board, row, col):
            if row == 9:
                if isValidSudoku(board):
                    return True
                return False
            
            if board[row][col] == '.': 
                for num in "987654321":
                    if num not in rows[row] and num not in cols[col] and num not in squares[(row // 3, col // 3)]:
                        board[row][col] = num
                        cols[col].add(board[row][col])
                        rows[row].add(board[row][col])
                        squares[(row // 3, col // 3)].add(board[row][col])
                        
                        if col < 8:
                            checker = backtrack(board, row, col + 1)
                        else:
                            checker = backtrack(board, row + 1, 0)
                        
                        if checker: 
                            return True
                        
                        cols[col].discard(board[row][col])
                        rows[row].discard(board[row][col])
                        squares[(row // 3, col // 3)].discard(board[row][col])
                        board[row][col] = '.'
            else:
                if col < 8:
                    checker = backtrack(board, row, col + 1)
                else:
                    checker = backtrack(board, row + 1, 0)
                    
                if checker: 
                    return True
                        
        
        backtrack(board, 0, 0)
                        
            
                
                        
            
        