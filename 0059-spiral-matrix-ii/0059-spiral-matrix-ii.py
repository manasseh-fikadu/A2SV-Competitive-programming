class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for i in range(n)] for j in range(n)]
        left = 0
        right = n - 1
        up = 0
        down = n - 1
        num = 1
        
        while left <= right and up <= down:
            # fill top of the matrix
            for i in range(left, right + 1):
                matrix[up][i] = num
                num += 1
            up += 1
            
            # fill the right side of the matrix
            for i in range(up, down + 1):
                matrix[i][right] = num
                num += 1
            right -= 1
            
            # fill bottom of the matrix
            for i in range(right, left - 1, -1):
                matrix[down][i] = num
                num += 1
            down -= 1
            
            # fill left side of the matrix
            for i in range(down, up - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
            
        return matrix
            
            
            
            
            
        