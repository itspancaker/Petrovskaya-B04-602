f = open("input.txt", "r")
a = f.readlines()
b = a[0].split()
s = int(a[2].strip())
k = 0
m = 1
c =2* int(b[0],s)
result = ''
f.close()
p = open("output.txt", "w")
if a[1].strip() == '+':
    for i in range(len(b)):
        b[i] = int(b[i], s)
        k += int(b[i])
    gah = abs(k)
    while gah > 0:
        zhenka = gah % s
        result = str(zhenka) + result
        gah = gah // s
    if k < 0:
        p.write('-' + result)
    if k > 0:
        p.write(result)
    if k == 0:
        p.write('0')

if a[1].strip() == '-':
    for i in range( len(b)):
        b[i] = int(b[i], s)
        c -= int(b[i])
        gah=abs(c)
    while gah > 0:
        zhenka = gah % s
        result = str(zhenka) + result
        gah = gah // s
    if c<0:
        p.write('-'+result)
    if c>0:
        p.write(result)
    if c==0:
        p.write('0')

if a[1].strip() == '*':
    for i in range(len(b)):
        b[i] = int(b[i], s)
        m *= int(b[i])
    gah = abs(m)
    while gah > 0:
        zhenka = gah % s
        result = str(zhenka) + result
        gah = gah // s
    if m < 0:
        p.write('-' + result)
    if m > 0:
        p.write(result)
    if m == 0:
        p.write('0')

p.close()