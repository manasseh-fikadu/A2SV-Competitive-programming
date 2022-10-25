class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isEnd = True

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        trie = Trie()
        trie.insert(pattern)
        res = []
        for query in queries:
            res.append(self.match(query, trie))
        return res

    def match(self, query, trie):
        node = trie.root
        for c in query:
            if c in node.children:
                node = node.children[c]
            elif c.isupper():
                return False
        return node.isEnd