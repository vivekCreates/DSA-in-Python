def min_cost_climbing_stairs(arr):
    dp = [None]*len(arr)
    dp[0],dp[1] = arr[0],arr[1]
    
    for i in range(2,len(arr)):
        dp[i] = arr[i] + min(dp[i-1],dp[i-2])
        
    return min(dp[-1],dp[-2])
    
    
    
cost = min_cost_climbing_stairs([10,20,5,2,1,12])
print("Min cost: ",cost)