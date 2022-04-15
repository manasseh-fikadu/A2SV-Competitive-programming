class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        adj = defaultdict(list)
        n = len(recipes)
        in_degree = defaultdict(int)
        
        for i in range(n):
            val = recipes[i]
            for ing in ingredients[i]:
                adj[ing].append(val)
                in_degree[val] += 1
                
        q = deque([i for i in supplies])
        
        while q:
            curr = q.popleft()
            for nei in adj[curr]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0: q.append(nei)
        ans=[]
        for recipe in recipes:
            if in_degree[recipe] <= 0: ans.append(recipe)
        return ans
        