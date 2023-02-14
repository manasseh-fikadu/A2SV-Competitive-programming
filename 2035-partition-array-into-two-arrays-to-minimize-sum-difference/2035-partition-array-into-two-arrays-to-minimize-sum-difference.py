class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 2

        arrayA = []
        for k in range(n+1):
            arrayA.append(sorted(sum(x) for x in combinations(nums[:n],k)))
        arrayB = []
        for k in range(n+1):
            arrayB.append(sorted(sum(x) for x in combinations(nums[n:],k)))

        _sum = sum(nums)
        halve = _sum / 2
        ans = float('inf')

        for k in range(n+1):
            partitionA = arrayA[k]
            partitionB = arrayB[n-k]
            for i in partitionA:
                j = bisect.bisect_left(partitionB, halve-i)
                if j < len(partitionB):
                    ans = min(ans, abs(_sum - 2 * (i + partitionB[j])))
                if j:
                    ans = min(ans, abs(_sum - 2 * (i + partitionB[j-1])))

        return ans