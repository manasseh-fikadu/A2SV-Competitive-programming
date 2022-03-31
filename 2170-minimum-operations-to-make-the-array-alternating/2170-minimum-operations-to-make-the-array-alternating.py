class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
#         odd, even = [], []
#         n = len(nums)
#         if len(nums) == 1:
#             return 0
#         for i in range(1, n, 2):
#             odd.append(nums[i])
#         for i in range(0, n, 2):
#             even.append(nums[i])
        
#         oddFreq = Counter(odd)
#         evenFreq = Counter(even)
                 
#         oddFreqList = oddFreq.most_common(2)
#         evenFreqList = evenFreq.most_common(2)
        
#         oddMax = oddFreqList[0][0]
#         evenMax = evenFreqList[0][0]
        
#         oddMaxFreq = oddFreqList[0][1]
#         if len(oddFreqList) > 1:
#             odd2ndMaxFreq = oddFreqList[1][1]
#         else:
#             odd2ndMaxFreq = 0
#         evenMaxFreq = evenFreqList[0][1]
#         if len(oddFreqList) > 1:
#             even2ndMaxFreq = evenFreqList[1][1]
#         else:
#             even2ndMaxFreq = 0
        
#         if oddMax != evenMax:
#             return n - oddMaxFreq - evenMaxFreq
        
#         return min(n - oddMaxFreq - even2ndMaxFreq, n - odd2ndMaxFreq - evenMaxFreq)

        odds = Counter()
        evens = Counter()
        for i, x in enumerate(nums):
            if i % 2 == 0:
                evens [x] += 1
            else:
                odds[x] += 1
        evenSums = sum(evens.values())
        oddSums = sum(odds.values())
        evenMaxes = list(sorted(evens.items(), key=lambda x: (-x[1], x[0])))
        oddMaxes = list(sorted(odds.items(), key=lambda x: (-x[1], x[0])))
        if len(oddMaxes) == 0:
            return 0
        if evenMaxes[0][0] == oddMaxes[0][0]:
            poss = 10 ** 10
            if len(oddMaxes) > 1:
                poss = min(poss, (evenSums - evenMaxes[0][1]) + (oddSums - oddMaxes[1][1]))
            else:
                poss = min(poss, (evenSums - evenMaxes[0][1]) + (oddSums))
            if len(evenMaxes) > 1:
                poss = min(poss, (evenSums - evenMaxes[1][1]) + (oddSums - oddMaxes[0][1]))
            else:
                poss = min(poss, (evenSums) + (oddSums - oddMaxes[0][1]))
            return poss
        else:
            return (evenSums - evenMaxes[0][1]) + (oddSums - oddMaxes[0][1])
    

                
                