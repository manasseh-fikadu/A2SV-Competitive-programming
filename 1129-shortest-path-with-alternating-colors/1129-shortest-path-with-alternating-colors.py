class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in redEdges:
            graph[u].append((v, 1))
        for u, v in blueEdges:
            graph[u].append((v, 0))
        q = deque([(0, 0, 0), (0, 1, 0)])
        visited = set()
        res = [-1] * n
        while q:
            u, color, dist = q.popleft()
            if (u, color) in visited:
                continue
            visited.add((u, color))
            if res[u] == -1:
                res[u] = dist
            for v, c in graph[u]:
                if c != color:
                    q.append((v, c, dist + 1))
        return res
        