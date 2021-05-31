def postorderTraversal(self, A):
    ret = []
    stack = []
    
    # sol 3 # using 2 stacks
    stack.append(A)
    while stack:
        top = stack.pop()
        if top.left: stack.append(top.left)
        if top.right: stack.append(top.right)
        ret.append(top)
    ans = []
    while ret: ans.append(ret.pop().val)
    return ans
    
    
    # sol 2 # using 1 stack
    root = A 
    while stack or root:
        if root != None:
            stack.append(root)
            root = root.left
        else:
            top = stack[-1]
            if (top.right and not ret) or (top.right and ret and top.right.val != ret[-1]):
                root = top.right
            else:
                ret.append(top.val)
                stack.pop()
    return ret
    
    
    # sol 1
    # preorder -> root left right
    # we can modify it as root right left
    # and after reverse we get left right root -> which is post order
    
    root = A
    while stack or root != None:
        if root != None:
            ret.append(root.val)
            stack.append(root)
            root = root.right
        else:
            top = stack.pop()
            root = top.left
    
    return ret[::-1]
                