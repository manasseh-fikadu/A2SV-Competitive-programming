class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = 0
        while i < len(pushed) and pushed:
            if pushed[i] == popped[0]:
                popped.pop(0)
                pushed.pop(i)
                i = max(i-1,0)
            else:
                i += 1
        if not pushed:
            return True
        else:
            return False
