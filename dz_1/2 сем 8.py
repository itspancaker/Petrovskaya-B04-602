n=int(input())
a=[int(x) for x in input().split()]
for x in a:
    m=0
    for y in a:
        if y<x:
           m+=1
    if m==n//2:
        print(x)
        break