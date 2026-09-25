n,b,c=map(int,input().split())
dec =0
power =0
result=''
while n>0:
    digit=n%10
    dec += digit *(b** power )
    n=n//10
    power+=1
while dec>0:
    zhenka=dec%c
    result=str(zhenka)+result
    dec=dec//c
print(result)