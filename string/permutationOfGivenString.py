def toString(List):
    return ''.join(List)

def permute(s,l,r):
    if l==r:
        print( toString(s) )
    else:
        for i in range(l,r+1):
            s[l],s[i] = s[i],s[l]
            permute(s,l+1,r) 
            s[l],s[i] = s[i],s[l] # Backtracking

if __name__ == "__main__":
    string = "ABC"
    s = list(string)
    permute(s,0,len(s)-1)



