def preorderTraversal(self, A):
    ans = []
    stack = []
    root = A
    while stack or root!=None:
        if root != None:
            ans.append(root.val)
            stack.append(root)
            root = root.left
        else:
            top = stack.pop()
            root= top.right
    
    return ans