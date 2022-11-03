class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        in_degree = [0] * n
        
        for orig, dest in edges:
            graph[orig].append(dest)
            in_degree[dest] += 1
                    
        output = [set() for _ in range(n)]
        
        queue = deque()
        for i in range(len(in_degree)):
            if not in_degree[i]:
                queue.append(i)
                
        while queue:
            curr = queue.popleft()
            for par in graph[curr]:
                output[par].add(curr)
                in_degree[par] -= 1
                
                for j in output[curr]:
                    output[par].add(j)
                if not in_degree[par]:
                    queue.append(par)
                        
        for i in range(len(output)):
            output[i] = sorted(output[i])
        return output
    