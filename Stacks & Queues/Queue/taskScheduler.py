class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequency = [values for values in Counter(tasks).values()]
        frequency.sort()
        maxNumber = max(frequency)
        
        final = (maxNumber-1) * (n+1)
        count = 0
        for v in frequency:
            if v == maxNumber:
                count += 1
                
        return max(final + count,len(tasks))
