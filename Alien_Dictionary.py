class Solution:
    def findOrder(self,dict, N, K):
        graph = {}
        for i in range(K):
            graph[chr(i+97)] = []
    
        indegree = [0] * K
    
        stack = []
    
        result = ""
    
        for i in range(N-1):
            word1 = dict[i]
            word2 = dict[i+1]
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    graph[word1[j]].append(word2[j])
                    indegree[ord(word2[j])-97] += 1
                    break
    
        for i in range(K):
            if indegree[i] == 0:
                stack.append(chr(i+97))
    
        while len(stack) > 0:
            node = stack.pop()
            result += node
            for i in range(len(graph[node])):
                indegree[ord(graph[node][i])-97] -= 1
                if indegree[ord(graph[node][i])-97] == 0:
                    stack.append(graph[node][i])
    
        return result
