import time

def fib(n, dp):
    if n <= 1:
        return n
    if dp[n] != 0:
        return dp[n]

    dp[n] = fib(n-1, dp) + fib(n-2, dp)
    return dp[n]

def nfib(n):
    dp = [0] * (n+1)
    return fib(n, dp)

start = time.time()
print(nfib(500))
end = time.time()

print("time:", end - start)
