# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
        
# Given a binary search tree A, where each node contains a positive integer, and an integer B, you have to find whether or not there exist two different nodes X and Y such that X.value + Y.value = B.

# Return 1 to denote that two such nodes exist. Return 0, otherwise.

class Solution:
	# @param A : root node of tree
	# @param B : integer
	# @return an integer
	def t2Sum(self, A, B):
        self.ptr1 = []
        self.ptr2 = []
        
        self.setPtr1(A)
        self.setPtr2(A)
        
        p1 = self.getPtr1()
        p2 = self.getPtr2()
        
        while p1 != p2:
            sum_ = p1.val + p2.val
            if sum_ == B: return 1
            
            if sum_ < B:
                p1 = self.getPtr1()
            else:
                p2 = self.getPtr2()
                
        return 0
    
    def getPtr1(self):
        if not self.ptr1: return -1
        top = self.ptr1.pop()
        if top.right:
            self.setPtr1(top.right)
        return top
    
    def getPtr2(self):
        if not self.ptr2: return -1
        top = self.ptr2.pop()
        if top.left:
            self.setPtr2(top.left)
        return top

    def setPtr1(self, node):
        curr = node
        while curr:
            self.ptr1.append(curr)
            curr = curr.left
    
    def setPtr2(self, node):
        curr = node
        while curr:
            self.ptr2.append(curr)
            curr = curr.right
    
    

