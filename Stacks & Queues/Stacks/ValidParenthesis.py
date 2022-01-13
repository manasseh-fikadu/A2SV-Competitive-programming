class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {'(' : ')', '{' : '}', '[' : ']'}
        if len(s) % 2 != 0:
            return False
        for i in s:
            if i in dict.keys():
                stack.append(i)
            else:
                if stack == []:
                    return False
                p = stack.pop()
                print(p)
                if i != dict[p]:
                    return False
        return stack == []
