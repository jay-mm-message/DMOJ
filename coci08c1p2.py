
exam_num = int(input())
exam_consists = list(input())
exam_current_max = 0

# Adrian
Adrian_exam_current_num = 0
for i in range(exam_num):
  if i % 3 == 0:
    if 'A' == exam_consists[i]:
      Adrian_exam_current_num = Adrian_exam_current_num + 1
  elif i % 3 == 1:
    if 'B' == exam_consists[i]:
      Adrian_exam_current_num = Adrian_exam_current_num + 1
  elif i % 3 == 2:
    if 'C' == exam_consists[i]:
      Adrian_exam_current_num = Adrian_exam_current_num + 1      

# Bruno
Bruno_exam_current_num = 0
for i in range(exam_num):
  if i % 4 == 0:
    if 'B' == exam_consists[i]:
      Bruno_exam_current_num = Bruno_exam_current_num + 1
  elif i % 4 == 1:
    if 'A' == exam_consists[i]:
      Bruno_exam_current_num = Bruno_exam_current_num + 1
  elif i % 4 == 2:
    if 'B' == exam_consists[i]:
      Bruno_exam_current_num = Bruno_exam_current_num + 1 
  elif i % 4 == 3:
    if 'C' == exam_consists[i]:
      Bruno_exam_current_num = Bruno_exam_current_num + 1 

# Goran
Goran_exam_current_num = 0
for i in range(exam_num):
  if i % 6 == 0:
    if 'C' == exam_consists[i]:
      Goran_exam_current_num = Goran_exam_current_num + 1
  elif i % 6 == 1:
    if 'C' == exam_consists[i]:
      Goran_exam_current_num = Goran_exam_current_num + 1
  elif i % 6 == 2:
    if 'A' == exam_consists[i]:
      Goran_exam_current_num = Goran_exam_current_num + 1 
  elif i % 6 == 3:
    if 'A' == exam_consists[i]:
      Goran_exam_current_num = Goran_exam_current_num + 1 
  elif i % 6 == 4:
    if 'B' == exam_consists[i]:
      Goran_exam_current_num = Goran_exam_current_num + 1 
  elif i % 6 == 5:
    if 'B' == exam_consists[i]:
      Goran_exam_current_num = Goran_exam_current_num + 1

exam_current_max = max(Adrian_exam_current_num, max(Bruno_exam_current_num, Goran_exam_current_num))

print(exam_current_max)
if exam_current_max == Adrian_exam_current_num:
  print('Adrian')
if exam_current_max == Bruno_exam_current_num:
  print('Bruno')
if exam_current_max == Goran_exam_current_num:
  print('Goran')

# print('Adrian_exam_current_num: ', Adrian_exam_current_num)
# print('Bruno_exam_current_num: ', Bruno_exam_current_num)
# print('Goran_exam_current_num: ', Goran_exam_current_num)