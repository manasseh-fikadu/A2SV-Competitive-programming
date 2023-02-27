class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        logs_count = Counter()
        for birth, death in logs:
            logs_count[birth] += 1
            logs_count[death] -= 1
        
        min_year = float('inf')
        max_pop = float('-inf')
        total = 0
        for year in sorted(logs_count.keys()):
            total += logs_count[year]
            if total > max_pop:
                max_pop = total
                min_year = year
                
        return min_year