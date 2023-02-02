class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        dict_ = {}
        for i in nums:
            if i != 0:
                dict_[i] = 1
        return sum(dict_.values())