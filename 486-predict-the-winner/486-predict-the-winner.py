class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def play(start, end):
            if start > end:
                return 0  

            s, e = nums[start], nums[end]
            l, r = play(start + 1, end), play(start, end - 1)

            return max(s - l, e - r)

        return play(0, len(nums) - 1) >= 0