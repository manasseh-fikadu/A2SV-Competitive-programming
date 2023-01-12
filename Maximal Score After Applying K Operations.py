class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        res = 0
        heap = heapify(nums)
        for _ in range(k):
            val = heappop(nums) * -1
            res += val
            heappush(nums, -math.ceil(val/3))
        return res
