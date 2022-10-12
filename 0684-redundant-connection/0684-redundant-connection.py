class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
#       BFS Implementation
        graph = defaultdict(list)
        for u, v in edges:
            if self.bfs(graph, u, v):
                return [u, v]
            graph[u].append(v)
            graph[v].append(u)
        return []

    def bfs(self, graph, u, v):
        if u not in graph:
            return False
        q = [u]
        visited = set()
        while q:
            node = q.pop(0)
            if node == v:
                return True
            visited.add(node)
            q.extend([nei for nei in graph[node] if nei not in visited])
        return False

