import time

def fibo(n):
    if n <=1:
        return n
    return fibo(n-1)+fibo(n-2)


start = time.time()
ans = fibo(40)
print(ans)
end = time.time()

print("time: ",end-start)
