class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for _str in strs:
            ans[tuple(sorted(_str))].append(_str)
        return ans.values()