class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        
        graph = defaultdict(list)
        for x, y in connections:
            graph[x].append(y)
            graph[y].append(x)
        
        seen = set()
        def dfs(i):
            for nei in graph[i]:
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei)
        ans = 0
        for i in range(n):
            if i not in seen:
                dfs(i)
                ans += 1
        return ans - 1