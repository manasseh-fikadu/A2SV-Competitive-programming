class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        length = len(satisfaction)
        dp = [[0 for _ in range(length)] for _ in range(length)]
        for d in range(length):
            dp[0][d] = satisfaction[d]
        for t in range(1, length):
            for d in range(t, length):
                dp[t][d] = dp[t-1][d-1] + satisfaction[d] * (t+1)
        return max([ele for row in dp for ele in row]+[0])