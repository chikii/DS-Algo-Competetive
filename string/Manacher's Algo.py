# Q) longest palindromic substring

def manacher(s):
    n = len(s)
    S = ['|']
    for i in s:
        S.append(i)
        S.append('|')
    
    N = len(S)
    Z = [0]*N
    
    center = radius = 0
    
    while center < N:
        
        while center-radius >= 0 and center+radius < N and S[center-radius] == S[center+radius]:
            radius += 1
        radius -= 1
        Z[center] = radius
        
        left = center-radius
        right = center+radius
        
        radius = 0
        center += 1
        while center < N and center <= right:
            mirror_center = right+left-center
            max_radius = right-center
            
            if Z[mirror_center] < max_radius:
                Z[center] = Z[mirror_center]
                center += 1
            elif Z[mirror_center] > max_radius:
                Z[center] = max_radius
                center += 1  
            else:
                radius = max_radius
                break
    r = 0
    for i in range(N):
        if r < Z[i]:
            r = Z[i]
            c = i
    
    return ''.join(S[c-r+1 : c+r+1 : 2])       
	                
	        



s = 'aaaaaaaaaaa'

print(manacher(s))

# ans is max(max(oddZ), max(evenz))