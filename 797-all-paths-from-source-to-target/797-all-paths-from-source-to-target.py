class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        
        for i, nodes in enumerate(graph):
            adj[i] = nodes
            
        def dfs(node, path):
            if node == len(graph) - 1:
                res.append(path)
                return

            for n in adj[node]:
                dfs(n, path + [n])

        res = []
        dfs(0, [0])
        
        return res
            