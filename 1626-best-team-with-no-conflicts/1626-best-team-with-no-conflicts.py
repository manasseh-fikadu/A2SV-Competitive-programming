class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        _zip = list(zip(ages, scores))
        _zip.sort()
        
        @lru_cache(None)
        def dp(i):
            nonlocal _zip
            res = _zip[i][1]
            for j in range(i + 1, len(scores)):
                if _zip[i][0] == _zip[j][0] or _zip[i][1] <= _zip[j][1]:
                    res = max(res, dp(j) + _zip[i][1])
            return res
        
        ans = 0
        for i in range(len(scores)):
            ans = max(ans, dp(i))
        return ans
        
        