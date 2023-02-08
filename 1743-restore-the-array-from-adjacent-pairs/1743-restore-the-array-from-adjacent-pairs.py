class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for pair in adjacentPairs:
            graph[pair[0]].append(pair[1])
            graph[pair[1]].append(pair[0])

        res = []
        start = 0
        for key in graph:
            if len(graph[key]) == 1:
                start = key
                break

        def dfs(start):
            res.append(start)
            if len(res) == len(adjacentPairs) + 1:
                return
            next_ = graph[start]
            if len(next_) == 1:
                dfs(next_[0])
            else:
                if next_[0] != res[-2]:
                    dfs(next_[0])
                else:
                    dfs(next_[1])

        dfs(start)
        return res