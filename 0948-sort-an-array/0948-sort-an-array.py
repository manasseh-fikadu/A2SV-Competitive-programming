class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merger(array1, array2, pointer1, pointer2, lists):
            if pointer1 == len(array1) and pointer2 == len(array2):
                return lists
            elif pointer1 == len(array1):
                return lists + array2[pointer2:]
            elif pointer2 == len(array2):
                return lists + array1[pointer1:]
            elif array1[pointer1] < array2[pointer2]:
                lists.append(array1[pointer1])
                return merger(array1, array2, pointer1 + 1, pointer2, lists)
            elif array1[pointer1] == array2[pointer2]:
                lists.append(array1[pointer1])
                lists.append(array2[pointer2])
                return merger(array1, array2, pointer1 + 1, pointer2 + 1, lists)
            else:
                lists.append(array2[pointer2])
                return merger(array1, array2, pointer1, pointer2 + 1, lists)
        
        def mergeSort(nums):
            if len(nums) <= 1:
                return nums
            middle = len(nums) // 2
            merged_array = merger(mergeSort(nums[:middle]), mergeSort(nums[middle:]), 0, 0, [])
            return merged_array
        
        return mergeSort(nums)
