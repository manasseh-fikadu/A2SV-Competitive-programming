class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if not edges or not edges[0]:
            return 0
        N = len(edges)
        graph = defaultdict(list)
        
        for [u,v] in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        for i in graph.keys():
            if len(graph[i]) == N:
                return i
        
        return 0