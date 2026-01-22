def print_pattern(n):
    if n == 0:
        return 0
    print_pattern(n-1)
    for i in range(n):
        print("#",end=" ")
    print(end="\n")
    
print_pattern(5)