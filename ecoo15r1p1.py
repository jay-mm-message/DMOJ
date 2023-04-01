

for dataset in range(10):  
  num_orange = 0
  num_blue = 0
  num_green = 0
  num_yellow = 0
  num_pink = 0
  num_violet = 0
  num_brown = 0
  num_red = 0

  colors = ''

  done = False
  
  while not done:
      info = input()
      if info == 'end of box':
        done = True
      else:
        colors = colors + ' ' + info

  # colors_list = colors.split()
  # colors = str(sorted(colors_list))
  # print('colors: ', colors)
  num_orange  = ((colors.count('orange') + 6)  // 7) * 13
  num_blue    = ((colors.count('blue')   + 6)  // 7) * 13
  num_green   = ((colors.count('green')  + 6)  // 7) * 13
  num_yellow  = ((colors.count('yellow') + 6)  // 7) * 13
  num_pink    = ((colors.count('pink')   + 6)  // 7) * 13
  num_violet  = ((colors.count('violet') + 6)  // 7) * 13
  num_brown   = ((colors.count('brown')  + 6)  // 7) * 13
  num_red     = colors.count('red')                  * 16

  total_num = 0
  total_num = total_num + num_orange
  total_num = total_num + num_blue
  total_num = total_num + num_green
  total_num = total_num + num_yellow
  total_num = total_num + num_pink
  total_num = total_num + num_violet
  total_num = total_num + num_brown
  total_num = total_num + num_red
  print(total_num)