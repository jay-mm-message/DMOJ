
times = int(input())
for dataset in range(times):
    line = input()

    i = 0 ; lines = ''
    while i < len(line):
        
        total = 1
        while i < (len(line) - 1) and line[i] == line[i+1]:
            total = total + 1
            i = i + 1
        lines = lines + f'{total} {line[i]} '
        i = i + 1
    
    print(lines)