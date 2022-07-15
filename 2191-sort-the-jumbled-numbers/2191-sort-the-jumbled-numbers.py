class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        d = defaultdict(list)
        n = len(nums)
        
        for i in range(n):
            str1 = str(nums[i])
            str2 = str()
            for j in str1:
                str2 += str(mapping[int(j)]) 

            d[int(str2)].append(nums[i])

        key = list(d.keys())
        key.sort() 
                
        result = []
        for i in key:
            result += d[i]
            
        return result