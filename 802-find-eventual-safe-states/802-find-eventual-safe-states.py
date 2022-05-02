class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe = defaultdict()

        def dfs(i):
            if i in safe:
                return safe[i]
            safe[i] = False
            for nei in graph[i]:
                if not dfs(nei):
                    return safe[i]
            safe[i] = True
            return safe[i]            

        ans = []
        for i in range(len(graph)):
            if dfs(i):
                ans.append(i)
        return ans
        