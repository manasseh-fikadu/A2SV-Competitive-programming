class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.endOfWord = True

    def search(self, word) -> bool:
        l = 0
        curr = self.root
        for char in word:
            if char in curr.children:
                l += 1
                curr = curr.children[char]
                if curr.endOfWord: break
            else: return 0
        return l
    

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        ans = sentence.split(" ")
        for i in range(len(ans)):
            word = ans[i]
            replace = trie.search(word)
            if replace:
                ans[i] = ans[i][:replace]
                
        return " ".join(ans)

        
        
            