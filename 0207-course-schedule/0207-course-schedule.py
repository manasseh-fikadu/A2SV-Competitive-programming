class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        DFS Implementation using two coloring
        '''
        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[u].append(v)
        color = [0] * numCourses
        
        def dfs(node):
            if color[node] == 1:
                return True
            if color[node] == 2:
                return False
            color[node] = 2
            for neigh in adj[node]:
                if not dfs(neigh):
                    return False
            color[node] = 1
            return True
        
        for node in range(numCourses):
            if not dfs(node):
                return False
        return True
        