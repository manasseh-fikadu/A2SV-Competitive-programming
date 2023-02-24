class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        pass_ = 0
        while True:
            for i in range(n):
                if tickets[i] == 0:
                    continue
                tickets[i] -= 1
                pass_ += 1
                if tickets[k] == 0:
                    return pass_