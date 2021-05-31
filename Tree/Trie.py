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
    
    def delete(self, word):
        root = self.root
        last = None
        stack = [(root, -1)]
        
        for ch in word:
            idx = ord(ch) - ord('a')
            if root.children[idx] == None: return # word is not present
            root = root.children[idx]
            stack.append((root, idx)) # idx of curr Child w.r.t parent, so to dlete me delete the idx of parent
            
        root.isWord = False # mark the word False

        while stack and stack[-1][0] != self.root:
            child = 0
            root, idx = stack.pop()

            if root.isWord: return
            
            for i in range(26):
                if root.children[i] != None: child += 1

            if child == 0:
                stack[-1][0].children[idx] = None
            else:
                return