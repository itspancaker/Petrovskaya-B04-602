n=input()
mp = 'AHIMOTUVWXY18'
ms = 'EJSZ3L25'
msf = 0
mpf = 0
rp = 0
if n[::-1] != n:
    print(f"{n} is not a palindrome.")
else:
    for i in n:
        if i not in ms and i not in mp:
            rp = 1
            break
        if i in ms:
            msf = 1
        if i in mp:
            mpf = 1
    if rp:
            print(f"{n} is a regular palindrome.")
    elif msf:
            print(f"{n} is a mirrored string.")
    else:
            print(f"{n} is a mirrored palindrome.")

