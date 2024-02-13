n, k = map(int, input().split())

while k > 0:
    
    n_10 = n%10
    if n_10 == 0:
        n //= 10
        k -= 1
    else: 
        if k < n_10:
            n -= k
        else:
            n -= n_10
        k -= n_10
 
    # if n%10 == 0:
    #     n //= 10
    # else: 
    #     n -= 1
        
    # k -= 1
    
print(n)


