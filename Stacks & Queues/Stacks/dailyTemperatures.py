class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        waiting_days = [0] * len(temperatures)
        stack = []
        
        for cur_idx, cur_t in enumerate(temperatures):
            while stack and cur_t > stack[-1][1]:
                prev_idx, prev_t = stack.pop()
                waiting_days[prev_idx] = cur_idx - prev_idx
            stack.append( (cur_idx, cur_t) )
            
        return waiting_days
