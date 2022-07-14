class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incomings = [0 for i in range(n)]
        for fro, to in edges:
            incomings[to] += 1
        
        ans = []
        for i in range(len(incomings)):
            if incomings[i] == 0:
                ans.append(i)
                
        return ans