class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        routes = [set(route) for route in routes]
        graph = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                graph[stop].add(i)
                
        queue = deque([(source, 0)])
        seen = {source}
        while queue:
            stop, count = queue.popleft()
            for i in graph[stop]:
                if target in routes[i]:
                    return count + 1
                for j in routes[i]:
                    if j not in seen:
                        seen.add(j)
                        queue.append((j, count + 1))
                routes[i].clear()
        return -1