l = [10,20,30,40,50]

def print_list(n,lt):
    if n == len(l): return
    print(lt[n])
    print_list(n+1,lt) 
    
    
print_list(0,l)
        