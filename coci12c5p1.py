# tone = 'CD|EC|CD|EC|EF|GEF|G|GAGF|EC|GAGF|EC|CG|C|CG|C'
# tone = 'AEB|C'
tone = input()

a_minor = 0
c_major = 0

for i in range(len(tone)):
  if i == 0 or tone[i-1] == '|':
    if tone[i] in 'ADE':
      a_minor = a_minor + 1
    if tone[i] in 'CFG':
      c_major = c_major + 1

if a_minor == c_major:
  if tone[-1] == 'A':
    a_minor = a_minor + 1
  else:
    c_major = c_major + 1

if a_minor > c_major:
  print('A-mol')
else:
  print('C-dur')