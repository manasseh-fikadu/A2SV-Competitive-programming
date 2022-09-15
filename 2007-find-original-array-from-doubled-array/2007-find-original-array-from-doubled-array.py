class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        original = []
        s = Counter(changed)
        for i in range(0, len(changed)):
            if changed[i] in s and (2*changed[i]) in s:
                original.append(changed[i])
                s[changed[i]] -= 1
                if s[changed[i]] == 0:
                    s.pop(changed[i])
                s[changed[i]*2] -= 1
                if s[changed[i]*2] == 0:
                    s.pop(changed[i]*2)
        if not s:
            return original