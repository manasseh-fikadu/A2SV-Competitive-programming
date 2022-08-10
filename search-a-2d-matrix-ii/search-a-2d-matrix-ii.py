class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            l, r = 0, len(matrix[0]) - 1
            while l <= r:
                mid = (l + r) // 2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] > target:
                    r = mid - 1 
                elif matrix[i][mid] < target:
                    l = mid + 1
        return False