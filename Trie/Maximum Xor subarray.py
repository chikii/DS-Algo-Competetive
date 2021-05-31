class TrieNode:
    def __init__(self):
        self.num = -1
        self.idx = -1
        self.childs = [None]*2
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, no, curr_idx):
        root = self.root
        for bit in range(31, -1, -1):
            idx = no&(1<<bit) != 0
            if not root.childs[idx]:
                root.childs[idx] = TrieNode()
            root = root.childs[idx]
        root.num = no
        root.idx = curr_idx
    
    def getMaxXor(self, no):
        root = self.root
        for bit in range(31, -1, -1):
            idx = no&(1<<bit) == 0
            if root.childs[idx]:
                root = root.childs[idx]
            else:
                root = root.childs[not idx]
        
        # idx+1, is neccessary, because, XOR[1 to N] ^ XOR[1 to (L-1)] = XOR[L to R] , where, 1 < l---r < N
        # we get a no with whome xor is maximum, that no is L-1, so to get the starting point(L), we need to do  L+1
        return no^root.num, root.idx+1
                

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A)
        
        ans = 0
        final_ans = [1, 1]
        
        trie = Trie()
        trie.insert(A[0], 0)
        xor = A[0]
            
        for i in range(1, n):
            xor ^= A[i]
            
            # case 1: if subarray starting with 1 is having max xor.
            if xor > ans:
                ans = xor
                final_ans = [1, i+1]
                
            # get the maximum xor
            temp_ans, idx = trie.getMaxXor(xor)
            # L - idx
            # R - XOR
            
            trie.insert(xor, i) # append curr xor in trie
            
            
            # case 2: L to R is maximum xor., we want minimum length subarray with less starting index
            if temp_ans >= ans:
                if temp_ans == ans:
                    k, l = final_ans
                    if i-idx < l-k:
                        final_ans = [idx+1, i+1]  #### +1, for 1 based indexing
                    elif i-idx == l-k and i<l:
                        final_ans = [idx+1, i+1]
                else:
                    ans = temp_ans
                    final_ans = [idx+1, i+1]
            
            
        
        return final_ans
        
