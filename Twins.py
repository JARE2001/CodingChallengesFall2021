
def twins(num, coins):

    dollars = 0
    for element in coins:
        dollars += element 
    
    coins.sort(reverse = True)
    print(coins)

    acum = 0
    count = 0

    for element in coins:
        if acum <= dollars/2:
            acum += element
            count += 1
    return count

num = input()
coins = input().split()

print(twins(num, coins))