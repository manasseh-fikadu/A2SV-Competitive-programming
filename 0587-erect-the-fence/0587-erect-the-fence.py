class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        trees.sort() 
        
        def cmpSlopes(p1, p2, p3):
            x1, y1 = p1
            x2, y2 = p2
            x3, y3 = p3
            return (y3 - y1) * (x2 - x1) - (y2 - y1) * (x3 - x1) 
        
        higher, lower  = [], []
        
        for point in trees:
            while len(higher) >= 2 and cmpSlopes(higher[-2], higher[-1], point) > 0:
                higher.pop() 
            while len(lower) >= 2 and cmpSlopes(lower[-2], lower[-1], point) < 0: 
                lower.pop() 
            
            lower.append(tuple(point)) 
            higher.append(tuple(point))   
        
        return set(lower + higher)