class Solution:
    def hIndex(self, citations: List[int]) -> int:
        cite = sorted(citations, reverse=True)
        
        for hi in range(len(cite)):
            if hi+1 > cite[hi]:
                return hi
            
        return len(cite)
