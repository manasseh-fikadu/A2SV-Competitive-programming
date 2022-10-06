class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = defaultdict(list)
        for orig, dest in richer:
            graph[dest].append(orig)
            
        ans = [0] * n
        def dfs(node):
            if ans[node] == 0:
                ans[node] = node
                for child in graph[node]:
                    cand = dfs(child)
                    if quiet[cand] < quiet[ans[node]]:
                        ans[node] = cand
            return ans[node]
        
        return map(dfs, range(n))