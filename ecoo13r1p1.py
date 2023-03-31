

next_num = int(input())
late_num = 0
waiting_num = 0

while True:
    words = input()
    
    if words == 'EOF':
        break

    if words == 'TAKE':

        late_num = late_num + 1
        waiting_num = waiting_num + 1
        next_num = next_num + 1

        if next_num == 1000:
            next_num = 1

    elif words == 'SERVE':
        waiting_num = waiting_num - 1

    elif words == 'CLOSE':
        print(late_num, waiting_num, next_num)
        late_num = 0
        waiting_num = 0

    elif words == 'EOF':
        break