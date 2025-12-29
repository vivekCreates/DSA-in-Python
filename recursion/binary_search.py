def binary_search(arr,l,r,target):
    while l <= r:
        mid = (l+r)//2
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            return binary_search(arr,mid+1,r,target)
        else:
            return binary_search(arr,l,mid-1,target)
        
        
l = [10,20,30,40,50]

ans = binary_search(l,0,4,20)
print(ans)