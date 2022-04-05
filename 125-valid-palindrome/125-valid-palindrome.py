class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack = []
        res, coll = "", ""
        for i in range(len(s)):
            if s[i].isalnum():
                stack.append(s[i].lower())
                coll += s[i].lower()
        for i in range(len(stack)):
            res += stack.pop()
            
        return True if res == coll else False