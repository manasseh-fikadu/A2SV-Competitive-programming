class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        conv_nums = []
        for i in range(0, len(nums)):
            conv_nums.append(int(nums[i]))
        conv_nums.sort()
        conv_nums.reverse()
        return str(conv_nums[k-1])
