class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        # freq = dict(Counter(arr).most_common())
        # counts = Counter(arr)
        # remaining = len(arr)
        # ans = set()
        # for k, v in freq.items():
        #     temp = freq
        #     remaining -= temp[k]
        #     ans.add(temp[k])
        #     if remaining <= len(arr) / 2:
        #         return len(ans)

        n = len(arr)
        occrs = Counter(arr)
        h = [-occrs[x] for x in occrs]
		
        heapq.heapify(h)
        deleted = 0
        uDeleted = 0
        
        while deleted < n / 2:
            uDeleted += 1
            deleted -= heapq.heappop(h)
        return uDeleted
            
        