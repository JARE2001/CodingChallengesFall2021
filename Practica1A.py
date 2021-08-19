def coinsToTake(n,values):
    values.sort()
    mid= sum(values)/2
    money,x = 0,0
    for i in range(len(values)-1, -1, -1):
        if money <= mid:
            money += values[i]
            x += 1
        else:
            return x
    return x

n = input()
values =input()

aux =[]
acum =""
for i in values:
    acum +=i
    if i == " ":
        aux.append(int(acum))
        acum =""
aux.append(int(acum))

print(coinsToTake(n,aux))