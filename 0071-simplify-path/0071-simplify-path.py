class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')
        for p in path:
            if p == '..':
                if len(stack) > 0:
                    stack.pop()
            elif p == '.' or p == '':
                continue
            else:
                stack.append(p)
        return '/' + '/'.join(stack)