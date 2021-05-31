def solve(self, A, B, C):
        curr = A
        
        while curr:
            if B < curr.val and C < curr.val:
                curr = curr.left
            elif B > curr.val and C > curr.val:
                curr = curr.right
            else:
                x = find(curr, B)
                y = find(curr, C)
                return x+y

def find(root, key):
    count = 0
    
    while root:
        if root.val == key:
            return count
        if key < root.val:
            root = root.left
        else:
            root = root.right
        count += 1