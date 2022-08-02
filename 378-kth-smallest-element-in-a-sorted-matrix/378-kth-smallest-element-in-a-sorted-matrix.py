class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []

        row, col = len(matrix), len(matrix[0])

        for i in range(row):
            heapq.heappush(heap, (matrix[i][0], 0, matrix[i]))

        while heap:
            val, idx, currow = heapq.heappop(heap)
            k -= 1
            if k == 0:
                return val
            if idx + 1 < col:
                heapq.heappush(heap, (currow[idx+1], idx+1, currow))