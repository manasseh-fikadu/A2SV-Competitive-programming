class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        occrs = Counter(arr)
        h = [-occrs[x] for x in occrs]
		
        heapq.heapify(h)
        print(h)
        deleted = 0
        uDeleted = 0
        
        while deleted < n // 2:
            uDeleted += 1
            deleted -= heapq.heappop(h)
        return uDeleted