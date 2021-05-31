
def morris_inOrder(root): 
    
    curr = root
    ans = None
    
    while curr != None:
        if curr.left == None:
            print(curr.val) # access
            curr = curr.right
        else:
            pred = curr.left
            while pred.right != None and pred.right != curr:
                pred = pred.right        
                
            if pred.right == None:
                pred.right = curr
                curr = curr.left
            else:
                pred.right = None
                print(curr.val) # access
                curr = curr.right
    return ans

# moris post order - # morris POST ORDER -> https://www.quora.com/What-is-a-good-way-to-implement-stackless-recursion-less-post-order-traversal-for-a-non-threaded-binary-tree-using-Morris-method   