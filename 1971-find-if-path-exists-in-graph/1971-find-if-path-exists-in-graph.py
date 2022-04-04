class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = defaultdict(list)
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
    
        def dfs(s):
            visited.add(s)
            for node in adj[s]:
                if node not in visited:
                    dfs(node)
        
        visited = set()
        dfs(source)
        if destination in visited:
            return True
        return False