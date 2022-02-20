class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # total number of subarrays: sum = k
        count = 0
        prefixSum = 0
        store = {0:1}
        
        for num in nums:
            prefixSum += num
            if prefixSum - k in store:
                count += store[prefixSum - k]
            if prefixSum not in store:
                store[prefixSum] = 1
            else:
                store[prefixSum] += 1
            
        return count
