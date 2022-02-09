class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        if len(num)==1:
            return "0"
        
        for n in num:
            while stack and stack[-1] > n and k > 0:
                stack.pop()
                k-=1
            stack.append(n)

        while k > 0 and stack:
            stack.pop()
            k-=1
        return "".join(stack).lstrip("0") or "0"
