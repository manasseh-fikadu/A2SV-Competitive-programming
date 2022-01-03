class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        copy = sorted(heights)
        count = 0
        for i in range(len(copy)):
            if copy[i]!=heights[i]:
                count += 1
        return count
