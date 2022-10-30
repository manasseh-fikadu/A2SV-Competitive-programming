class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        if k == 1:
            return nums
        if k == len(nums):
            return [max(nums)]
        result = []
        queue = collections.deque()
        for i in range(len(nums)):
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)
            if queue[0] == i - k:
                queue.popleft()
            if i >= k - 1:
                result.append(nums[queue[0]])
        return result