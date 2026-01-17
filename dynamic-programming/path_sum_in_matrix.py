def paths(arr, r, c,dp):
    n = len(arr)
    m = len(arr[0])

    if r < 0 or c < 0 or r >= n or c >= m:
        return -1000000  

    if r == n - 1:
        return arr[r][c]
    
    if dp[r][c]!=-1: return dp[r][c]

    left = paths(arr, r + 1, c - 1,dp)
    down = paths(arr, r + 1, c,dp)
    right = paths(arr, r + 1, c + 1,dp)
    dp[r][c] = arr[r][c] + max(left, down, right)
    return dp[r][c]


mat = [[2, 7],
       [9, 15]]

def path_sum(mat,m,n):
    dp = [[-1 for _ in range(n)] for _ in range(m)]
    return max(paths(mat, 0, c,dp) for c in range(len(mat[0])))

ans = path_sum(mat,len(mat),len(mat[0]))
print("ans:", ans)
