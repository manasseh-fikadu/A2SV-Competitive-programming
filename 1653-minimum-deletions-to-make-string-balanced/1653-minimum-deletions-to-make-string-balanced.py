class Solution:
    def minimumDeletions(self, s: str) -> int:
        res = 0
        stack = []
        
        for char in s:
            if char == "a":
                if stack:
                    stack.pop()
                    res += 1
            else: 
                stack.append(char)
                
        return res