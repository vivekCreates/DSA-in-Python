def paths(m,n,dp):
    if m==1 and n==1: 
        return 1
    if m==0 or n==0: 
        return 0
    
    if dp[m][n]!=-1: 
        return dp[m][n]
     
    dp[m][n] = paths(m,n-1,dp) + paths(m-1,n,dp)
    return dp[m][n]
    

def number_of_paths(m,n):
    dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]
    return paths(m,n,dp)
    
    
ans = number_of_paths(10,10)

print("number of ways: ",ans)