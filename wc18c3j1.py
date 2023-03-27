p = int(input())
b = int(input())
sell_d = int(input())

money = (p // b) * sell_d + (p % b)
print(money)