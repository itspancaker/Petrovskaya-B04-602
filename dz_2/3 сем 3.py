def f(a, b):
    if b == 0:
        return 1, 0, a
    x1, y1, d = f(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return x, y, d
while True:
    try:
        line = input()
        parts = line.split()
        if len(parts) == 0:
            continue
        a = int(parts[0])
        b = int(parts[1])
        x,y,d = f(a,b)
        if a==b:
            x y = 0,1
        print(f"{x} {y} {d}")
    except EOFError:
        break