apple_three = int(input())
apple_two = int(input())
apple_one = int(input())

banana_three = int(input())
banana_two = int(input())
banana_one = int(input())

apple_total = (apple_three * 3) + (apple_two * 2) + (apple_one * 1)
banana_total = (banana_three * 3) + (banana_two * 2) + (banana_one * 1)

#print('apple_total: %d' % apple_total, ", banana_total: %d" % banana_total)
if apple_total > banana_total:
    print('A')
elif banana_total > apple_total:
    print('B')
else:
    print('T')