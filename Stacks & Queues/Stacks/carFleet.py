class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        
        coll = list(zip(position,speed))
        coll.sort()
        print(coll)
        
        for pos,spe in coll:
            time = (target - pos) / spe
                        
            while stack and stack[-1] <= time:
                stack.pop()
            
            stack.append(time)
                        
        return len(stack)
