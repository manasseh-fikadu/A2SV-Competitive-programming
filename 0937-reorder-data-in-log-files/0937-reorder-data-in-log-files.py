class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def keyGen(log):
            word, int_ = log.split(" ", 1)
            if int_[0].isalpha():
                return (0, int_, word)                 
            else:
                return (1,)
        return sorted(logs, key=keyGen)