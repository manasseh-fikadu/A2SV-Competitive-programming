class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(node):
            seen.add(node)
            for neighbor in graph[node]:
                if neighbor not in seen:
                    dfs(neighbor)
        
        graph = defaultdict(list)
        
        for i in range(len(rooms)):
            for key in rooms[i]:
                graph[i].append(key)
                
        seen = set()
        dfs(0)  # Start DFS from room 0
        
        return len(seen) == len(rooms)
