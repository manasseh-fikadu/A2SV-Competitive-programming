class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        graph = collections.defaultdict(list)
        
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
            
        visited = set()
        def dfs(root, parent):
            visited.add(root)
            for node in graph[root]:
                if node == parent: 
                    continue
                if node in visited:
                    return False
            
                if not dfs(node, root):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n
