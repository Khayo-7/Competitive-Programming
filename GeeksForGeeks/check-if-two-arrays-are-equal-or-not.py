#Function to check if two arrays are equal or not.
def check(self,A,B,N):
    
    if len(A) != len(B) or len(set(A)) != len(set(B)):
        return 0
        
    len_A = len(A)
    len_B = len(B)
    
    if len_A > len_B:
        A, B = B, A
    
    B_new = {}
    for b in B:
        if b in B_new:
            B_new[b] += 1
        else:
            B_new[b] = 1
        
    for a in A:
        if a in B_new:
            if B_new[a] > 1:
                B_new[a] -= 1
            else:
                B_new.pop(a)
            
        else:
            return 0
    else:
        return 1