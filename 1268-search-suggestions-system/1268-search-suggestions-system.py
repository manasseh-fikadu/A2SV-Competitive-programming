class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        self.wordStore = ""

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = TrieNode()

        def insert(word) -> None:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.endOfWord = True
            curr.wordStore = word

        def finder(prefix):
            def dfs(node):
                if node.endOfWord:
                    candidates.append(node.wordStore)
                for child in node.children:
                    dfs(node.children[child])

            curr = root
            for char in prefix:
                if char in curr.children:
                    curr = curr.children[char]
                else:
                    return []
            candidates = []
            dfs(curr)
            candidates.sort()
            return candidates[:3]

        for word in products:
            insert(word)
        
        ans = []
        prefix = ""
        for c in searchWord:
            prefix += c
            ans.append(finder(prefix))

        return ans