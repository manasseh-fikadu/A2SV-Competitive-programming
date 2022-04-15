class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        
        for l in prerequisites:
            adj[l[1]].append(l[0])
        
        indegrees = [0] * (numCourses)
        
        for key in adj:
            for node in adj[key]:
                indegrees[node] += 1
                
        q = []
        
        for i,val in enumerate(indegrees):
            if val == 0:
                q.append(i)
        
        res = []
        
        while q:
            s = q.pop(0)
            res.append(s)
            for j in adj[s]:
                indegrees[j] -= 1
                if indegrees[j] == 0:
                    q.append(j)
        
        if len(res) != numCourses:
            return []
        return res