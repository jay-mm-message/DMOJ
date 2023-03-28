
words = input()
mach_position = 0
total = 0

for char in words:
  if mach_position == 0:
    mach = 'H'
  elif mach_position == 1:
    mach = 'O'
  elif mach_position == 2:
    mach = 'N'
  elif mach_position == 3:
    mach = 'I'

  if mach == char:
    mach_position = mach_position + 1
    if mach_position == 4:
      mach_position = 0
      total = total + 1

print(total)