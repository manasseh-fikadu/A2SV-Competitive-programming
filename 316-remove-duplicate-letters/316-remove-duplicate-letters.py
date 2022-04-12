class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lastIndex = {}
        for i, ch in enumerate(s):
            lastIndex[ch] = i
        
        stack = []
        for i, ch in enumerate(s):
            if ch not in stack:
                while stack and stack[-1] > ch and lastIndex[stack[-1]] > i:
                    stack.pop()
                stack.append(ch)
        return ''.join(stack)