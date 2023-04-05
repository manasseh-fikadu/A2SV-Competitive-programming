class Solution:
    def permute(self, a: List[int]) -> List[List[int]]:
        n = len(a)
        target = (1 << n) - 1
        res = []
        v = []
        def recur(mask):
            nonlocal res, v
            if target == mask:
                res.append(list(v))
                return
            for i in range(n):
                if (mask & (1 << i)) == 0:
                    v.append(a[i])
                    recur(mask | (1 << i))
                    v.pop()
        recur(0)
        return res