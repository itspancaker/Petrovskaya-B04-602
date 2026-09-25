n=input().split()
m=int(n[0])
k=0
for i in range(1,m):
    k+=int(n[i])
l=m*(m+1)/2
print(int(l-k))
