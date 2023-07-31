class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        memo = {}

        def compute_cost(i, j):
            if i < 0 and j < 0:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]
            
            if i < 0:
                memo[(i, j)] = ord(s2[j]) + compute_cost(i, j-1)
                return memo[(i, j)]
            if j < 0:
                memo[(i, j)] = ord(s1[i]) + compute_cost(i-1, j)
                return memo[(i, j)]
            
            if s1[i] == s2[j]:
                memo[(i, j)] = compute_cost(i-1, j-1)
            else:
                memo[(i, j)] = min(
                    ord(s1[i]) + compute_cost(i-1, j),
                    ord(s2[j]) + compute_cost(i, j-1)
                )

            return memo[(i, j)]

        return compute_cost(len(s1)-1, len(s2)-1)