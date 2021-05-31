# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Node:
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def flatten(self, A):
        solve(A)
        return A
    
def solve(root):
    if root == None: return Node()
    
    left = solve(root.left)
    right = solve(root.right)
    
    root.left = None
    
    if left.head == None:
        root.right = right.head
        
        ret = Node(root)
        if right.tail == None:
            ret.tail = root
        else:
            ret.tail = right.tail
            
        return ret
    else:
        root.right = left.head
        left.tail.right = right.head
        
        ret = Node(root)
        if right.tail != None:
            ret.tail = right.tail
        else:
            ret.tail = left.tail

        return ret
    
    
    
    
    
    
