class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
#         DFS Implementation
        graph = defaultdict(list)
        for u, v in edges:
            if self.dfs(graph, u, v, set()):
                return [u, v]
            graph[u].append(v)
            graph[v].append(u)
        return []

    def dfs(self, graph, u, v, visited):
        if u not in graph:
            return False
        if u in visited:
            return False
        visited.add(u)
        if u == v:
            return True
        return any(self.dfs(graph, nei, v, visited) for nei in graph[u])

