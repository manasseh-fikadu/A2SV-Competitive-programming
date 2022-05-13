class Solution:
    def reverseBits(self, n: int) -> int:
        
        def binary2int(binary): 
            int_val, i, n = 0, 0, 0
            while(binary != 0): 
                a = binary % 10
                int_val = int_val + a * pow(2, i) 
                binary = binary//10
                i += 1
            return int_val
            
        res = ''
        for i in range(32):
            flip = (n >> i) & 1
            res += str(flip)
        return binary2int(int(res))