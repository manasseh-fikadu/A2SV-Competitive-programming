class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = [-1] * len(nums1)
        
        for i in range(len(nums1)):
            n = nums2.index(nums1[i])
            for j in range(n, len(nums2)):
                if nums2[j] > nums1[i]:
                    stack[i] = nums2[j]
                    break
                    
        return stack
