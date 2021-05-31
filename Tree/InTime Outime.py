def InTimeOutTime(self, A, B, C): # InTimeOutTime
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