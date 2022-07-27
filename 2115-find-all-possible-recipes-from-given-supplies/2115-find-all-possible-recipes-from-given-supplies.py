class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        adj_list = defaultdict(list)
        indegree = defaultdict(int)
        n = len(recipes)
        
        for i in range(n):
            val = recipes[i]
            for ing in ingredients[i]:
                adj_list[ing].append(val)
                indegree[val] += 1
                
        queue = deque([i for i in supplies])
        ans = []
        
        while queue:
            cur = queue.popleft()
            for j in adj_list[cur]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    queue.append(j)
                    ans.append(j)
                    
        return ans

        