class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        curr_time = 0
        result = 0
        seeds = sorted(range(len(plantTime)), key=lambda x: -growTime[x]) 
        for seed in seeds:
            curr_time += plantTime[seed]
            result = max(result, curr_time + growTime[seed])
        return result
        