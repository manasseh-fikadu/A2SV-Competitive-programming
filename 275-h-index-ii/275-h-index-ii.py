class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left, right = 0, len(citations)-1
        n = len(citations)
        
        while left <= right: 
            mid = left + (right - left)//2
            currCite = n - mid
            h_index = citations[mid]
            
            if h_index < currCite:
                left = mid + 1
            elif h_index > currCite:
                right = mid - 1
            else:
                return h_index
            
        return n - left