n = input().split()
a=0
b=0
for i in range(len(n)):
    if n.count(n[i]) > a:
        a = n.count(n[i])
        b = n[i]
print(b)