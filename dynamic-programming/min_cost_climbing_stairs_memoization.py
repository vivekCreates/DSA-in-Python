

def min_cost(arr,i,dp):
    if i>=len(arr):
        return 0
    if dp[i]!=-1:
        return dp[i]
    
    dp[i] = arr[i] + min(min_cost(arr,i+1,dp),min_cost(arr,i+2,dp))
    return dp[i]


def min_cost_climbing_stairs(arr):
    dp = [-1]* len(arr)
    return min(min_cost(arr,0,dp),min_cost(arr,1,dp))

ans = min_cost_climbing_stairs([10,20,5,2])
print("Min cost: ",ans)