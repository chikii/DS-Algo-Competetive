class SegmentTree:
    def __init__(self, n):
        self.tree = [0]*(4*n)
        
    def build(self, s, e, node_idx, A):
        if s == e:
            self.tree[node_idx] = A[s]
            return
        
        mid = (s+e)//2
        li = (2*node_idx) + 1 
        ri = li+1
        
        self.build(s, mid, li, A)
        self.build(mid+1, e, ri, A)
        
        self.tree[node_idx] = self.tree[li]+self.tree[ri]
    
    def update(self, s, e, node_idx, idx, val, A):
        if idx<s or e<idx: return
        if s==e:
            A[idx] = val
            self.tree[node_idx] = val
            return
        
        mid = (s+e)//2
        li = (2*node_idx) + 1
        ri = li+1
        self.update(s, mid, li, idx, val, A)
        self.update(mid+1, e, ri, idx, val, A)
        self.tree[node_idx] = self.tree[li]+self.tree[ri]

    def query(self, s, e, l, r, node_idx):
        
        # no overlap 
        if e<l or r<s: return 0
        
        # full overlap
        if l<=s and e<=r: return self.tree[node_idx]
        
        # partial overlap
        mid = (s+e)//2
        li = (2*node_idx) + 1
        ri = li+1
        
        left = self.query(s, mid, l, r, li)
        right = self.query(mid+1, e, l, r, ri)
        
        return left+right

n = 4
Stree = SegmentTree(n)