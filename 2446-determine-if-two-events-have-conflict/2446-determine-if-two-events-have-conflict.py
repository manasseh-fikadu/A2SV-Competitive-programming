class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        return max(event1, event2)[0] <= min(event1, event2)[1]