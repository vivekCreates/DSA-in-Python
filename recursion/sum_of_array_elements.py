l = [1,2,3,4,5]

def sum_of_list(n,lt):
    if n < 0: 
        return 0
    return lt[n] + sum_of_list(n-1,lt)

print(sum_of_list(4,l))