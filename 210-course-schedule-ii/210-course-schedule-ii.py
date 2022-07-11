class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
#         adj = defaultdict(list)
#         indegrees = [0] * (numCourses)
#         q = []
#         res = []
        
#         for l in prerequisites:
#             adj[l[1]].append(l[0])
        
#         for key in adj:
#             for node in adj[key]:
#                 indegrees[node] += 1
                        
#         for i,val in enumerate(indegrees):
#             if val == 0:
#                 q.append(i)
                
#         while q:
#             s = q.pop(0)
#             res.append(s)
#             for j in adj[s]:
#                 indegrees[j] -= 1
#                 if indegrees[j] == 0:
#                     q.append(j)
        
#         if len(res) != numCourses:
#             return []
#         return res
        inDegrees = [0] * numCourses
        outgoing = defaultdict(set)
        for course, pre in prerequisites:
            outgoing[pre].add(course)
            inDegrees[course] += 1

        queue = deque()
        for i in range(numCourses):
            if inDegrees[i]==0:
                queue.append(i)

        res = []
        while queue:
            course = queue.popleft()
            res.append(course)
            for neighbor in outgoing[course]:
                inDegrees[neighbor]-=1
                if inDegrees[neighbor]==0:
                    queue.append(neighbor)
        if len(res) != numCourses: return []
        return res