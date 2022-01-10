class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}
        for (cs, ct) in zip(s, t):
            if d1.get(cs) is None and d2.get(ct) is None:
                d1[cs] = ct
                d2[ct] = cs
            else:
                if d1.get(cs) != ct or d2.get(ct) != cs:
                    return False
        return True
