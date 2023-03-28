pw = input()

if len(pw) < 8 or len(pw) > 12:
  print('Invalid')
else:
  digit_count = 0
  lower_count = 0
  upper_count = 0

  for p in pw:
      if p.islower():
        lower_count = lower_count + 1
      elif p.isupper():
        upper_count = upper_count + 1
      elif p.isdigit():
        digit_count = digit_count + 1

  if not lower_count >= 3:
    print('Invalid')
  elif not upper_count >= 2:
    print('Invalid')
  elif not digit_count >= 1:
    print('Invalid')
  else:
    print('Valid') 