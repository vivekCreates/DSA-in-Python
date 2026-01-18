arr = [6, 5, 1, 7, 4]

def max_loot(arr):
    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return arr[0]

    dp = [0] * n
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])

    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + arr[i])

    print(dp)
    return dp[-1]

loot = max_loot(arr)
print(loot)
