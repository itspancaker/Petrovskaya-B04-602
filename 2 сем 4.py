a=input().split()
a[:len(a)//2*2:2], a[1::2] = a[1::2], a[:len(a)//2*2:2]
print(a)