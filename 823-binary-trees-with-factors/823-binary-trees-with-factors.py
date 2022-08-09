class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        counts = Counter(arr)
        arr.sort()
        
        for i, num in enumerate(arr):
            for left in arr[:i]:
                quotient, reminder = divmod(num, left)
                if quotient <= 1: break
                if reminder == 0 and quotient in counts:
                    counts[num] += counts[left] * counts[quotient]
        
        return sum(counts.values()) % (10**9 + 7)