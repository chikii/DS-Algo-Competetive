# Q) longest palindromic substring

"""# this is for odd length palindrom, taking each element as center once."""
def manacher(s):
    n = len(s)
    z = [0]*n

    l = 0
    r = -1 # intialize with -1, because this will hit our first case i>r, for i = 07
    #  with the help of k we are mainiting left and right pointer for checking palindrom
    for i in range(n):
        if i>r: # run brute force
            k = 1 # because single element is also a plaindrom
        else: 
            # we need to have the mirror index of i and from that its longest palindrom, so we can start directly from there,
            # but this longest palindorm can not exceed our current j, beccause we don't know anything after curr R.
            j = l+r-i # mirror index of i
            k = min(r-i+1, z[j])

        # i-k = left pointer
        # i+k = right pointer
        while 0<= i-k and i+k<n and s[i-k] == s[i+k]:
            k += 1 

        z[i] = k
        k -= 1 
        # decrease the k by one because that particular is not matched that's by we break above loop, so we have to remove that one extra count.

        # l and r is denoting the last maximum palindorm
        if i+k > r:
            l = i-k
            r = i+k

    return z


def manacher_even(s): # for even length
    n = len(s)
    z = [0]*n

    l = 0
    r = -1
    for i in range(n):
        if i>r:
            k = 0 # in even length we can not have a palindrom of 1 length
        else:
            j = r+l-i+1
            k = min(r-i+1, z[j])
        
        # i-k-1 # is always a better choice then i+k+1
        while 0<= i-k-1 and i+k < n and s[i-k-1] == s[i+k]:
            k += 1

        z[i] = k
        k -= 1

        if i+k>r:
            l = i-k-1
            r = i+k
    
    return z



s = 'aaaaaaaaaaa'

print(manacher_even(s))

# ans is max(max(oddZ), max(evenz))