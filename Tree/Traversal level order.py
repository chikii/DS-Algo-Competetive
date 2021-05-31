    
def levelOrder2(self, A): # using que
    if A is None: return []
    
    que = deque()
    que.append(A)
    ret = []
    
    # we are marking end of level ->
    # At any given point, if we reach previous end. next End of level is always be the curr last node of que.
    end = A
    level = []
    while que:
        node = que.popleft()
    
        level.append(node.val)
        if node.left:
            que.append(node.left)
        if node.right:
            que.append(node.right)
                
        if node == end:
            ret.append(level)
            if que: end = que[-1]
            level = []
    
    return ret