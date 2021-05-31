# 2 values swapped in BST, find those value.

def inOrder(self, root): # O(H)
    if root == None: return
    
    self.inOrder(root.left)
    
    if self.prv > root.val:
        if self.swapA == None:
            self.swapA = self.prv
            self.swapB = root.val
        else:
            self.swapB = root.val
            return
        
    self.prv = root.val
    self.inOrder(root.right)