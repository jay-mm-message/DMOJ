Bears_A = int(input())
Bears_B = int(input())
Bears_C = int(input())

Max = max(Bears_A, max(Bears_B, Bears_C))
Min = min(Bears_A, min(Bears_B, Bears_C))

if (Bears_A != Max) and (Bears_A != Min):
    print(Bears_A)
elif (Bears_B != Max) and (Bears_B != Min):
    print(Bears_B)
else:
    print(Bears_C)
