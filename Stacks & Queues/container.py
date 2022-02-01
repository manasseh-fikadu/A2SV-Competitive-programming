class Solution:
    def maxArea(self, height: List[int]) -> int:
        output = 0
        
        left, right = 0, len(height) - 1
        while left < right:
            height1 = min(height[right], height[left])
            width = right - left
            area = height1 * width
            
            output = max(area, output)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return output
