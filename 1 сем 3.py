a=input().split()
b=1
for i in range(len(a)):
    b=b*int(a[i])
print(b**(1/len(a)))
