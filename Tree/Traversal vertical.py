def verticalOrderTraversal(self, A):
        if A is None: return []
        
        ret = {}
        que = deque()
        que.append((A,0))
        
        s = float('inf')
        e = -float('inf')
        
        while que:
            node, line = que.popleft()
            s = min(line, s)
            e = max(line, e)
            
            if node.left:
                que.append((node.left, line-1))
            if node.right:
                que.append((node.right, line+1))
            
            if ret.get(line) == None:
                ret[line] = [node.val]
            else:
                ret[line].append(node.val)
 
        ans = []
        for i in range(s, e+1):
            ans.append(ret[i])
        
        return ans

