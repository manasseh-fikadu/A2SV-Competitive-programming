class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        res = []
        for i in arr2:
            res.extend([i]*count[i])
            del count[i]
        for j in sorted(count.keys()):
            res.extend([j]*count[j])
        return res
