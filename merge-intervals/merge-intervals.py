class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        sorted_intervals = sorted(intervals, key = lambda x: x[0])
        result = [sorted_intervals[0]]
        for i in sorted_intervals:
            if i[0] <= result[-1][1]:
                result[-1][1] = max(i[1], result[-1][1])
            else:
                result.append(i)
        return result
        