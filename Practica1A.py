
def coinsToTake(n,values):
    values.sort()
    totalM = sum(values)
    money,x = 0,0
    for i in range(len(values)-1, -1, -1):
        if money <= totalM/2:
            money += values[i]
            x += 1
        else:
            return x
    return x


coins = [3,3]
print( coinsToTake(2, coins) )