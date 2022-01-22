class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Brute Force way
        stack = [-1] * len(nums1)
        
        for i in range(len(nums1)):
            n = nums2.index(nums1[i])
            for j in range(n, len(nums2)):
                if nums2[j] > nums1[i]:
                    stack[i] = nums2[j]
                    break
                    
        return stack
    
    
    # Updated with a Monotonic Stack Context
    greater = {}
        stack = []
        
        for num in nums2:
            while stack and stack[-1] < num:
                greater[stack.pop()] = num
            stack.append(num)
            
        return [greater.get(num, -1) for num in nums1]
