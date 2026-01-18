arr = [7,15,8,9,17]

def maximum_sum(arr):
    dp = [-1]* len(arr)
    return loot(0,arr,dp)


def loot(i,arr,dp):
    if i>=len(arr):
        return 0
    if dp[i]!= -1:
        return dp[i]
    
    pick = arr[i] + loot(i+2,arr,dp)
    skip = loot(i+1,arr,dp)
    ans = max(pick,skip)
    dp[i] = ans
    return ans


print("loot: ",maximum_sum(arr))