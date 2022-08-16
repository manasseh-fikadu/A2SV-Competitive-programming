class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        digits = set("0123456789")
        repeat = 0
        
        for char in s:
            if char == "]":
                item = stack.pop()
                curr = []
                
                while not isinstance(item, int):
                    curr.append(item)
                    item = stack.pop()
                stack += (curr[::-1] * item)
            elif char in digits:
                repeat = repeat * 10 + int(char)
            elif char == "[":
                stack.append(repeat)
                repeat = 0
            else:
                stack.append(char)
                
        return "".join(stack)