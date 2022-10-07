class Solution:
    def singleNonDuplicate(self, arr: List[int]) -> int:
        low = 0
        high = len(arr) - 1
        while low < high:
            mid = (low + high) // 2
            if mid % 2 == 0:
                if arr[mid] == arr[mid + 1]:
                    low = mid + 2
                else:
                    high = mid
            else:
                if arr[mid] == arr[mid - 1]:
                    low = mid + 1
                else:
                    high = mid - 1
        return arr[low]