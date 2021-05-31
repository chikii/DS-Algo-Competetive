def InOrder(A, ret):
    stack = []
    root = A
    while stack or root != None:
        if root != None:
            stack.append(root)
            root = root.left
        else:
            top = stack.pop()
            ret.append(top.val)
            root = top.right
    
    return ret
 
def inOrder(A, ret): #rec
    if A == None: return
    inOrder(A.left, ret)
    ret.append(A.val)
    inOrder(A.right, ret)   