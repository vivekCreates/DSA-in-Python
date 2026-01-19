mat = [
    [ 3, 6, 1],
    [ 2, 3, 4],
    [ 5, 5, 1],
    [ 6, 8, 3]
]

def path_sum_in_matrix(arr):
    m = len(arr)
    n = len(arr[0])
    
    dp = [[None for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0:
                dp[i][j] = arr[i][j]
            else:
                if  j == 0:
                    dp[i][j] = arr[i][j] + max(dp[i-1][j],dp[i-1][j+1])
                elif j == n-1:
                    dp[i][j] = arr[i][j] + max(dp[i-1][j-1],dp[i-1][j])
                else:
                    dp[i][j] = arr[i][j] + max(dp[i-1][j-1],dp[i-1][j],dp[i-1][j+1]) 
    return max(dp[-1])
    


max_sum = path_sum_in_matrix(mat)
print("Max sum: ",max_sum)