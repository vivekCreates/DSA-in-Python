def pre_in_post(n):
    if n == 0:
        return
    
    print(n)
    pre_in_post(n-1)
    print(n)
    pre_in_post(n-1)
    print(n)
    
    
    
pre_in_post(3)