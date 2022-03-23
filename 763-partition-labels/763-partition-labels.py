class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        
        for i, val in enumerate(s):
            last[val] = i
                    
        res = []
        curr = end = sums = 0 
        while end < len(s):
            end = max(end, last[s[curr]])
            start = curr
            while curr < end:
                end = max(end, last[s[curr]])
                curr += 1
            if curr == end:
                res.append(end - start + 1)
                print(res)
                sums += res[-1]
                if sums == len(s):
                    return res
                curr += 1