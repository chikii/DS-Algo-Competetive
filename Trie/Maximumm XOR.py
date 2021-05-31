# Q) Given an array of integers A, find and return the maximum result of A[i] XOR A[j], where i, j are the indexes of the array.

class TrieNode:
    def __init__(self):
        self.no = -1
        self.childs = [None]*2

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, num):
        root = self.root
        for bit in range(31, -1, -1):
            idx = num&(1<<bit) != 0
            if root.childs[idx] == None:
                root.childs[idx] = TrieNode()
            root = root.childs[idx]
        root.no = num
    
    def get_max_xor(self, num):
        root = self.root
        
        # do for all bit
        for bit in range(31, -1, -1):
            # get curr bit
            idx = num&(1<<bit) == 0
            # go oposite to that bit if child is present
            if root.childs[idx] != None:
                root = root.childs[idx]
            # else go to whichever child is present
            else:
                root = root.childs[not idx]
        return num^root.no
        
        
        
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        if n <= 1: return 0
        trie = Trie()
        trie.insert(A[0])
        xor = -float('inf')
        
        for i in range(1, n):
            xor = max(xor, trie.get_max_xor(A[i]))
            trie.insert(A[i])
        
        return xor
        
