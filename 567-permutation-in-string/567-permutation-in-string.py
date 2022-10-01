class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Counts = Counter(s1)
        window = len(s2) - len(s1) + 1
                            
        for i in range(window):
            s2Counts = Counter(s2[i:i+len(s1)])
            if s1Counts == s2Counts:
                return True
            
        return False
    
    '''

    for i in range(len(s2)-window+1):
        s2_c = Counter(s2[i:i+window])
        if s2_c == s1_c:
            return True

    return False
    '''
