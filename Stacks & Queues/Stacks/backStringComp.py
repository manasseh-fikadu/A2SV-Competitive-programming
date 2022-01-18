class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = ""
        t1 = ""
        
        for i in s:
            if i == "#":
                if len(s1)!=0:
                    s1 = s1[:len(s1)-1]  
            else:
                s1 = s1 + i
            
        for j in t:
            if j == "#":
                if len(t1)!=0:
                    t1 = t1[:len(t1)-1]
            else:
                t1 = t1 + j 
        
        return s1==t1
