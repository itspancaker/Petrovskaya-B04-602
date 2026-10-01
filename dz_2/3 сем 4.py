def triangle(size, symb):
    for i in range((size // 2) + 2):
        print(symb * i)

    for i in range(size // 2, 0, -1):
        print(symb * i)
a = input().split()
size = int(a[0])
symb = a[1]
triangle(size, symb)