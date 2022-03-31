class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
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
    

                
                