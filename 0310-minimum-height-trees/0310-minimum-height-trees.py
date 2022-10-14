class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        '''
        at most 2 MHTs are possible in any graph
        '''
        if n == 1:
            return [0]
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        leaves = []
        for i in range(n):
            if len(graph[i]) == 1:
                leaves.append(i)
        print(leaves)
        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for i in leaves:
                j = graph[i].pop()
                graph[j].remove(i)
                if len(graph[j]) == 1:
                    newLeaves.append(j)
            leaves = newLeaves
        return leaves
        