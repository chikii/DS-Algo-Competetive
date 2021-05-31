from heapq import heappush as push, heappop as pop

class stream:
    
    def __init__(self):
        self.max = []
        self.min = []
    
    def insert(self, elem):
        if not self.max:
            push(self.max, -elem)
            return
        
        if elem <= -self.max[0]:
            push(self.max, -elem)
            if len(self.max) > len(self.min)+1:
                push(self.min, -pop(self.max))
        else:
            push(self.min, elem)
            if len(self.min) > len(self.max):
                push(self.max, -pop(self.min))
    
    def median(self):
        return -self.max[0]

def solve(self, A):
        n = len(A)
        ans = []
        s = stream()
        
        for i in range(n):
            s.insert(A[i])
            ans.append(s.median())
        return ans
