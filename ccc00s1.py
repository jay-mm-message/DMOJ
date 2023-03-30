quarters = int(input())

first = int(input())
second = int(input())
third = int(input())

current_machine = 0
played_time = 0
while quarters != 0:
    quarters = quarters - 1
    played_time = played_time + 1
    current_machine = current_machine + 1

    if current_machine % 3 == 1:
        first = first + 1
    elif current_machine % 3 == 2:
        second = second + 1
    elif current_machine % 3 == 0:
        third = third + 1

    if first == 35:
        first = 0
        quarters = quarters + 30
    elif second == 100:
        second = 0
        quarters = quarters + 60
    elif third == 10:
        third = 0
        quarters = quarters + 9

print(f'Martha plays {played_time} times before going broke.')