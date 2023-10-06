class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        def comparator(a, b):
            if a+b > b+a:
                return -1
            else:
                return 1

        nums = list(map(str, nums))
        nums.sort(key=functools.cmp_to_key(comparator))
        largest_num = ''.join(nums)
        return '0' if largest_num[0] == '0' else largest_num
