N=int(input())
#способ 1
def fibonacci(N, cache={0:0,1:1}):
    if N in cache:
        return cache[N]
    else:
        cache[N] = fibonacci(N-1, cache) + fibonacci(N-2, cache)
        return cache[N]
print(fibonacci(N))
#способ 2
def fibionacci(N):
    if N<=1:
        return N
    a = 1
    b = 0
    for i in range(N-1):
        a, b = a+b, a
    return a
print(fibionacci(N))
