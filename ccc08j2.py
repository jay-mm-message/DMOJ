
playlist = ['A', 'B', 'C', 'D', 'E']

press_button = 0
loop = True
times = 0

while loop:
    press_button = int(input())
    times = int(input())

    if press_button == 1:
      shift = 1
      for t in range(times):
        playlist = playlist[shift:] + playlist[:shift]
    if press_button == 2:
      shift = 1
      for t in range(times):
        playlist = playlist[-shift:] + playlist[:-shift]
    if press_button == 3:
      for t in range(times):
        playlist[0], playlist[1] = playlist[1], playlist[0]
    if press_button == 4:
      playlist_to_strings = ' '.join(playlist)
      for t in range(times):
        print(playlist_to_strings)
      loop = False