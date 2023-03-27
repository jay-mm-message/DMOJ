H = ':-)'
S = ':-('

message = input()

if H not in message and S not in message:
  print('none')
else:
  h_count = message.count(H)
  s_count = message.count(S)

  if h_count > s_count:
    print('happy')
  elif s_count > h_count:
    print('sad')
  else:
    print("unsure")