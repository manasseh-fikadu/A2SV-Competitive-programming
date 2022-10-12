class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and len(trust) == 0:
            return 1
        elif len(trust) == 0:
            return -1
        else:
            trusters = []
            trusted = []
            for i in range(len(trust)):
                trusters.append(trust[i][0])
                trusted.append(trust[i][1])
            for i in range(1, n+1):
                if i not in trusters and trusted.count(i) == n-1:
                    return i
            return -1