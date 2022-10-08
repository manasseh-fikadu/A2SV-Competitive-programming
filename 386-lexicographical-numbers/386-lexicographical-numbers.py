class TrieNode():
    
    def __init__(self):
        self.children = {}
        self.is_end = False
        

class Solution:
    
    def __init__(self):
        self.trie_root = TrieNode()
        self.result_list = []
    
    def build_trie(self, s):
        
        c_node = self.trie_root
        for c in s:
            if(c not in c_node.children):
                c_node.children[c] = TrieNode()
            c_node = c_node.children[c]
            
        c_node.is_end = True
        
    def print_trie(self, c_node, cs):
        
        if(c_node.is_end):
            self.result_list.append(int(cs))
        
        for c, n_node in c_node.children.items():
            self.print_trie(n_node, cs+c)
        
        return
    
    
    
    def lexicalOrder(self, n: int) -> List[int]:
        
        for i in range(1, n+1):   
            s = str(i)
            self.build_trie(s)
        
        self.print_trie(self.trie_root, '')
        
        return self.result_list
        