class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        indegree = defaultdict(int)
        res = []
        queue = deque()

        for i, nei in enumerate(graph):
            indegree[i] = len(nei)
            if indegree[i] == 0:
                queue.append(i)
            for j in nei:
                adj_list[j].append(i)

        while queue:
            top = queue.popleft()
            res.append(top)
            for node in adj_list[top]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    queue.append(node)

        res.sort()
        return res
        
        
        