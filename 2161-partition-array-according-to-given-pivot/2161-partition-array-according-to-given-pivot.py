class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lt, eq, gt = [], [], []
        for i in range(len(nums)):
            if nums[i] == pivot:
                eq.append(nums[i])
            elif nums[i] > pivot:
                gt.append(nums[i])
            elif nums[i] < pivot:
                lt.append(nums[i])
                
        return lt + eq + gt