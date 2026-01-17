

def number_of_paths(row,col,m,n):
    if row==n or col==m:
        return 1
    rightways = number_of_paths(row,col+1,m,n)
    downways = number_of_paths(row+1,col,m,n)
    return rightways + downways
    
    
    
ans = number_of_paths(1,1,2,3)
print("number of ways: ",ans)