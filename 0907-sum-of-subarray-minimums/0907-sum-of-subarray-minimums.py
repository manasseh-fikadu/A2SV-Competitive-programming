class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        arr = [0] + arr + [0]
        res = 0
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                cur = stack.pop()
                res += arr[cur] * (i - cur) * (cur - stack[-1])
            stack.append(i)
        return res % (10 ** 9 + 7)