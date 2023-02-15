class Solution:
    def checkValidString(self, s: str) -> bool:
        if not s:
            return True
        if s == "*":
            return True
        if len(s) == 1:
            return False
        stack = []
        for i in s:
            if i == '(' or i == '*':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        stack = []
        for i in s[::-1]:
            if i == ')' or i == '*':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                else:
                    return False
        return True