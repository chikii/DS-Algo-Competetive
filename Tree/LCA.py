# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @param B : integer
	# @param C : integer
	# @return an integer
    def lca(self, A, B, C): # InTimeOutTime
        self.time = 0
        
        def traverse(root):
            if root == None: return
            
            inTime[root.val] = self.time
            self.time += 1
            
            traverse(root.left)
            traverse(root.right)
            
            outTime[root.val] = self.time
            self.time += 1
        
        inTime = {}
        outTime = {}
        traverse(A)
        #fuck lca
	
	def lca2(self, A, B, C): # recurrsive
	    anc_b = []
	    anc_c = []
	    
	    def getAnc(root, key, anc_list, org):
	        if root == None: return
	        
	        anc_list.append(root.val)
	        
	        if root.val == key:
	            org.extend(anc_list[:])
	            return
	        
	        getAnc(root.left, key, anc_list, org)
	        getAnc(root.right, key, anc_list, org)
	        
	        anc_list.pop()
	    
	    
	    getAnc(A, B, [], anc_b)
	    getAnc(A, C, [], anc_c)
	    lca = -1
	    for i in range(min(len(anc_b), len(anc_c))):
	        if anc_b[i] != anc_c[i]:
	            break
	        lca = anc_b[i]
	    
	    return lca
	           
	    