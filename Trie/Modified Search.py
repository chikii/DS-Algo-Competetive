# Given two arrays of strings A of size N and B of size M.

# Return a binary string C where C[i] = '1' if B[i] can be found in dictionary A using exactly one modification in B[i], Else C[i] = '0'.

# NOTE: modification is defined as converting a character into another character.


class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = [None]*26
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        root =self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if root.children[idx] == None:
                root.children[idx] = TrieNode()
            root = root.children[idx]
        root.isWord = True
    
    # flag will maintain the change, in word
    def dfs(self, root, curr_idx, word, n, flag):
        if flag>1: return False # step is very important, as soon as we found more than one change we break, else, 25*L vala factor will increase.
        
        if curr_idx == n:
            return flag == 1 and root.isWord == True
            
        for idx, child in enumerate(root.children):
            if child != None :
                ch = chr(idx+ord('a'))
                if word[curr_idx] != ch:
                    flag += 1
                
                if self.dfs(child, curr_idx+1, word, n, flag): return True
                
                if word[curr_idx] != ch:
                    flag -= 1
                
                    
                    
        return False
        

class Solution:
    # @param A : list of strings
    # @param B : list of strings
    # @return a strings
    def solve(self, A, B):
        trie = Trie()
        for i in A:
            trie.insert(i)
        ans = []
        for i in B:
            if trie.dfs(trie.root, 0, i, len(i), 0):
                ans.append('1')
            else:
                ans.append('0')
        return ''.join(ans)
        

"""
    # Time Complexity
    N - len(A)
    M = len(B)
    L = maximum length string in A or B
    
    Naive -> N*M*L
    
    Optimized -> 25*M*L*L
    
    1) create a trie on A, 
        O(N*L) - Time
        O(26^L) - at max we can have 26 level, and we can have 26 children of each node, consider if all level are filled.
        
    2) L is at max 20
       now, if we consider a change(can put different letter) position at every index then total string can be ->20*25
       why 25, there are 26 letters total and we need to put different letter. so ramining is 25
    
    
    3) we search all possible string(20*25) in trie, 
        Time Complexity search in trie - O(hieght of trie), O(L) in our case.
    
    4) we do this for all words in B - O(M)
    
    Total Time -> M(for all words) * L*25( total string possible with single string) * L (search in trie)
                = M*L*25*L
                = 25*M*(L^2)
                = M*(L^2)
                    
"""
    
    
    
    
    
    
    