class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        _set = set(sentence)
        if len(_set) == 26: return True
        else: False