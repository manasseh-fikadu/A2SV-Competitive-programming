class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProduct = nums[0]
        minProduct = nums[0]
        maxProductSoFar = nums[0]
        for i in range(1, len(nums)):
            temp = maxProduct
            maxProduct = max(nums[i], maxProduct * nums[i], minProduct * nums[i])
            minProduct = min(nums[i], temp * nums[i], minProduct * nums[i])
            maxProductSoFar = max(maxProductSoFar, maxProduct)
        return maxProductSoFar