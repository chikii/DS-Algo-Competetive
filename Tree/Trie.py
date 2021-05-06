class TrieNode:
    def __init__(self):
        self.freq = 0
        self.children = [None]*26
        # index  = ord(ch)-ord('a')

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, name):
        root = self.root
        for ch in name:
            idx = ord(ch)-ord('a')
            if root.children[idx] == None:
                root.children[idx] = TrieNode()
            root = root.children[idx]
            root.freq += 1
    
    def search(self, name):
        root = self.root
        for ch in name:
            idx = ord(ch)-ord('a')
            if root.children[idx] == None:
                return 0
            root = root.children[idx]
        return root.freq