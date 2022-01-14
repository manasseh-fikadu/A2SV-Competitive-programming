class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in s:
            if i != ')':
                stack.append(i)
            else:
                s = ''
                while(stack != [] and stack[-1] != '('):
                    s += stack.pop()
                stack.pop()
                stack.append(s[::-1])
        for i in range(len(stack)):
            stack[i] = stack[i][::-1]
        return "".join(stack)
