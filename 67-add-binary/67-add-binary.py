class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = int(a, 2), int(b, 2)
        xor = a ^ b
        carry = (a & b) << 1
        
        return str(bin(xor + carry)[2:])