class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        begin = [(start, -height, end) for start, end, height in buildings]
        begin += list({(end, 0, 0) for _, end, _ in buildings}) 
        begin.sort() 
        res = [[0, 0]] #[x, height]

        maxheap = [(0, float("inf"))] # [-height, ending position]
        for start, H, end in begin: 
            while maxheap[0][1] <= start: 
                heappop(maxheap)
            if H:
                heappush(maxheap, (H, end))

            if res[-1][1] != -maxheap[0][0]:
                res += [[start, -maxheap[0][0]]]
                
        return res[1:]
        
        