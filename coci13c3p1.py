
n = int(input())

a = 1
b = 0

for i in range(n):
    a,b = b,a+b

print(a,' ', b)