class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        
        def findPaths(x, y):
            
            if (x,y) in cache:
                return cache[(x,y)]
            
            if x == m-1 or y == n-1:
                return 1
            elif x >=m or y>=n:
                return 0
            else:
                cache[(x,y)] = findPaths(x+1,y) + findPaths(x, y+1)
                return cache[(x,y)]
            
        return findPaths(0,0)
            
            
            
            
            
            
            