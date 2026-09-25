n, s = input().split()
n = int(n)
result = [s[n*k:n*(k+1)] for k in range(0, len(s) // n)]
k=''
for i in result:
    k+=i[::-1]
print(k)
