def number_of_paths(m,n):
    dp = [[None for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0  or j ==0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]
    
paths = number_of_paths(4,4)
print("number of paths: ",paths)