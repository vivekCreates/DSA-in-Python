

def paths(m,n,dp):
    if m==1 and n==1: return 1
    if m==0 or n==0: return 0
    return paths(m-1,n,dp) + paths(m,n-1,dp)
    
    

def number_of_paths(m,n):
    dp = [-1]* (m*n)
    print(dp)
    return paths(m,n,dp)
    
    
ans = number_of_paths(3,3)
print("number of ways: ",ans)