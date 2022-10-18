class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            return self.count(self.countAndSay(n-1))

    def count(self, s):
        count = 1
        result = ""
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                count += 1
            else:
                result += str(count) + s[i]
                count = 1
        result += str(count) + s[-1]
        return result
    