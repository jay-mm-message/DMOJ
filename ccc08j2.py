
name_list = ['A', 'B', 'C', 'D', 'E']

button = 0
times = 0
loop = True

while loop:
    button = int(input())
    times = int(input())
    if button == 1:
      while times != 0:
        tmp = name_list[0]
        for i in range(1, len(name_list), 1):
            # print(name_list[i])
            name_list[i - 1] = name_list[i]
        name_list[-1] = tmp
        #print(name_list)
        times = times - 1

    elif button == 2:
      while times != 0:
        tmp = name_list[-1]
        for i in range(2, len(name_list) + 1, 1):
            name_list[-i + 1] = name_list[-i]
        name_list[0] = tmp
        #print(name_list)
        times = times - 1

    elif button == 3:
      while times != 0:
        name_list[0], name_list[1] = name_list[1], name_list[0]
        #print(name_list)
        times = times - 1
    
    elif button == 4:
      while times != 0:
        answer_string = ' '.join(name_list)
        print(answer_string)
        times = times - 1
      loop = False
   
#print(name_list)