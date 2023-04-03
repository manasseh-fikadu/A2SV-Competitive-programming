from sortedcontainers import SortedList

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        list_ = SortedList()
        counts = defaultdict(int)
        ans = 0
        
        for i in range(len(instructions)):
            list_.add((instructions[i], i))
            position = list_.index((instructions[i], i))
            ans += min(position - counts[instructions[i]], i - position) % (10**9 + 7)
            counts[instructions[i]] += 1
            
        return ans % (10**9 + 7)
        