class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        directions = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }
        visited = set()
        
        def dfs(current_row, current_col):
            visited.add((current_row, current_col))
            
            if (current_row, current_col) == (len(grid) - 1, len(grid[0]) - 1):
                return True 
            
            is_valid_path = False
            for r_offset, c_offset in directions[grid[current_row][current_col]]:
                new_row, new_col = current_row + r_offset, current_col + c_offset
                
                if new_row < 0 or new_col < 0 or new_row >= len(grid) or new_col >= len(grid[0]):
                    continue 
                
                if (new_row, new_col) in visited:
                    continue 
                
                next_path_type = grid[new_row][new_col]
                if (-r_offset, -c_offset) in directions[next_path_type]:
                    is_valid_path = is_valid_path or dfs(new_row, new_col)
            
            return is_valid_path
        
        return dfs(0, 0)
