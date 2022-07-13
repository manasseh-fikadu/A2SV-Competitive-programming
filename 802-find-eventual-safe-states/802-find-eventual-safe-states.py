class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adj_lst = {}
        outcome_count = {}
        queue = deque()
        res = []
        
        for i, nei in enumerate(graph):
            outcome_count[i] = len(nei)
            if not outcome_count[i]:
                queue.append(i)
            for j in nei:
                adj_lst.setdefault(j, []).append(i)
                
        while queue:
            node = queue.popleft()
            res.append(node)
            for nei in adj_lst.get(node, []):
                outcome_count[nei] -= 1
                if not outcome_count[nei]:
                    queue.append(nei)
        
        res.sort()
        return res
        