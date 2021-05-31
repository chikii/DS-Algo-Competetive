# Q)      1 -> NULL
    #    /  \
    #   2 -> 5 -> NULL
    #  / \  / \
    # 3->4->6->7 -> NULL

def connect(self, root): ## O(N), O(1)

        p = root

        while p != None:
            q = p
            # 1) assuming curr level next pointer is fixed
            # 2) so< will use above level next pointers to move to next childs
            
            while q != None:
                # 1) if left and right child present attach them and move next node in that level using next pointer
                
                if q.left:
                    if q.right:
                        q.left.next = q.right
                    else:
                        # if not right child mark left.next to first child found in 'q' level
                        q.left.next = self.getNext(q.next) # q.next is very imp, keeping it q will make infinite loop, hence it will give its own left/right child, we want next's first child.
                
                # if right child mark right.next to first child found in 'q' level
                if q.right:
                    q.right.next = self.getNext(q.next)
                
                q = q.next
            
            while p != None and p.left == None and p.right == None:
                p = p.next
            if p:
                if p.left: p = p.left
                else: p = p.right
            
        return root  
        
def getNext(self, q): # first child found in curr level
    while q:
        if q.left:
            return q.left
        if q.right:
            return q.right
        q = q.next