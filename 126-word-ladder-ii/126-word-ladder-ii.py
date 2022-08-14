class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return [] 
            
        n = len(beginWord)
        
        con = defaultdict(list) 
        if beginWord not in wordList: 
            for i in range(n):
                con[beginWord[:i]+"*"+beginWord[i+1:]].append(beginWord)
        for w in wordList:
            for i in range(n):
                con[w[:i]+"*"+w[i+1:]].append(w)
        
        curStack = set([endWord]) 
        visited = set(endWord)
        
        reverse = defaultdict(list) 
        beginNotFound = True  
        
        while curStack and beginNotFound:
            nextStack = set()
            for w in curStack:
                if w == beginWord:
                    beginNotFound = False
                    break
                for i in range(n):
                    for nw in con[w[:i]+"*"+w[i+1:]]:
                        if nw not in visited:
                            nextStack.add(nw)
                            reverse[nw].append(w)
            visited.update(nextStack) 
            curStack = nextStack
       
        ans = set()
        def DFS(w, path):
            for nw in reverse[w]:
                path.append(nw)
                if nw != endWord:
                    DFS(nw,path)
                else:
                    ans.add(tuple(path))
                path.pop()
        DFS(beginWord,[beginWord])
        
        return list(ans)
        
        