def zigzagLevelOrder(self, A):
    if A == None: return A
    
    ret = []
    curr_level = [A]
    next_level = []
    d = 0
    
    level = []
    while curr_level:
        
        node = curr_level.pop()
        level.append(node.val)
        if d == 0:
            if node.left: next_level.append(node.left)
            if node.right: next_level.append(node.right)
        else:
            if node.right: next_level.append(node.right)
            if node.left: next_level.append(node.left)
        
        if not curr_level:
            ret.append(level)
            level = []
            curr_level = next_level[:]
            next_level = []
            d = not d
            
            
    return ret