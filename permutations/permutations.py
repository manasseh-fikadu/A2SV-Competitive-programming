class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = [[]]
        
        for num in nums:
            temp = []
            for perm in permutations:
                for i in range(len(perm) + 1):
                    temp.append(perm[:i] + [num] + perm[i:])
            permutations = temp
            
        return permutations