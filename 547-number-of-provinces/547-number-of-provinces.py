class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited, provinces = [False] * n, 0

        def dfs(start):
            visited[start] = True

            for v, connected in enumerate(isConnected[start]):
                if connected and not visited[v]:
                    dfs(v)

        for i in range(n):
            if not visited[i]:
                provinces += 1
                dfs(i)

        return provinces