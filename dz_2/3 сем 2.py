n=int(input())
def factor(n,i=2):
    while (i*i<=n):
        if n%i:
            i+=1
        else:
            return [i]+factor(n//i,i)
    return [n]
print(factor(n))