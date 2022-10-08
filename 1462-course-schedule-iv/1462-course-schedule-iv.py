class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        neighbors = {node: set() for node in range(numCourses)}   
        indegree = defaultdict(int)     
        pre_lookup = defaultdict(set)  

        for pre, post in prerequisites:
            neighbors[pre].add(post)
            indegree[post] += 1
        
        queue = deque([])
        for n in neighbors:
            if indegree[n] == 0:
                queue.append(n)
        
        while queue:
            cur = queue.popleft()
            for neighbor in neighbors[cur]:
                pre_lookup[neighbor].add(cur)                   
                pre_lookup[neighbor].update(pre_lookup[cur])   
                
                indegree[neighbor] -= 1        
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        result = [True if q[0] in pre_lookup[q[1]] else False for q in queries]
        
        return result
        