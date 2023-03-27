month = int(input())
day = int(input())

S = 'Special'
A = 'After'
B = 'Before'

if month == 2 and day == 18:
  print(S)
elif month == 2 and day > 18:
  print(A)
elif month > 2:
  print(A)
else:
  print(B)
