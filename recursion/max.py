nums = [5,67,87,6,44]

def max_num(n,nums):
    if n < 0:
        return n
    return max(nums[n],max_num(n-1,nums))
    
    
print(max_num(len(nums)-1,nums))