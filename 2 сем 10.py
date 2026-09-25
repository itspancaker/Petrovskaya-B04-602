with open("input.txt", "r", encoding="utf-8") as f:
    text = f.readlines()
f3= open('file3.txt', 'w', encoding="utf-8")
ans = []
glas = 'еэоаыяиюу'
sogl = 'йцкнгшщзхъфвпрлджбьтмсч'
#glas = 'euoai'
#sogl = 'qwrtyplkjhgfdszxcvbnm'
for i in text:
    s = ''
    if i[0] in glas and i[1] not in glas:
        s+=i[0] + 'с' + i[0]
    else:
        s+=i[0]
    for j in range(1, len(i)):
        if i[j] in glas and i[j-1] in sogl:
            s+=i[j] + 'с' + i[j]
        else:
            s+=i[j]
    #print(s)
    ans.append(s)
#print(ans)
f3.writelines(ans)

