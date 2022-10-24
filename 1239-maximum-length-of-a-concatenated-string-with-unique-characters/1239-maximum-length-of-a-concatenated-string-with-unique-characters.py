class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.max_len = 0
        self.backtrack(arr, 0, '')
        return self.max_len

    def backtrack(self, arr, index, curr):
        if self.isUnique(curr):
            self.max_len = max(self.max_len, len(curr))
            for i in range(index, len(arr)):
                self.backtrack(arr, i + 1, curr + arr[i])

    def isUnique(self, s):
        return len(set(s)) == len(s)