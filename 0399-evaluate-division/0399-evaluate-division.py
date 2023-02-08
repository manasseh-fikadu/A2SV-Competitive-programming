class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (a, b), v in zip(equations, values):
            graph[a][b] = v
            graph[b][a] = 1.0 / v
            
        result = []
        for a, b in queries:
            if a not in graph or b not in graph:
                result.append(-1.0)
            else:
                result.append(self.dfs(a, b, graph, set()))
        return result

    def dfs(self, a, b, graph, visited):
        if a == b:
            return 1.0
        visited.add(a)
        for c in graph[a]:
            if c not in visited:
                v = self.dfs(c, b, graph, visited)
                if v > 0:
                    return v * graph[a][c]
        return -1.0
        