class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        copy = sorted([(intervals[i], i) for i in range(len(intervals))])
        res = [-1] * len(intervals)
        for interval, i in copy:
            left, right = 0, len(intervals)
            
            while left < right:
                mid = (left + right) // 2
                if copy[mid][0][0] < interval[1]:
                    left = mid + 1
                else:
                    right = mid
                    
            if left == len(intervals):
                continue
            res[i] = copy[left][1]
            
        return res
        