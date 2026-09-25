a=list(map(int, input().split()))
b=input()
c=0
d=1
if b=='+':
    for i in range(len(a)):
        c+=a[i]
    print(c)
if b=='-':
    for i in range(len(a)):
        c-=a[i]
    print(c)
if b=='*':
    for i in range(len(a)):
        d*=a[i]
    print(d)
