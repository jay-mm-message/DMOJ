swap_operation = input()

cups = [1, 0, 0]


for sw in swap_operation:
  if sw == 'A':
    cups[0], cups[1] = cups[1], cups[0]
  elif sw == 'B':
    cups[1], cups[2] = cups[2], cups[1]
  elif sw == 'C':
    cups[0], cups[2] = cups[2], cups[0]

if cups[0] == 1:
  print(1)
elif cups[1] == 1:
  print(2)
elif cups[2] == 1:
  print(3)