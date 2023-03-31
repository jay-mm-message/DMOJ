
exam_num = int(input())
exam_consists = list(input())
exam_current_max = 0

ADRIAN  = 'ABC'
BRUNO   = 'BABC'
GORAN   = 'CCAABB'

Adrian_exam_current_num = 0
Bruno_exam_current_num = 0
Goran_exam_current_num = 0

for i in range(exam_num):
# Adrian
  if exam_consists[i] == ADRIAN[i % len(ADRIAN)]:
    Adrian_exam_current_num = Adrian_exam_current_num + 1
# Bruno
  if exam_consists[i] == BRUNO[i % len(BRUNO)]:
    Bruno_exam_current_num = Bruno_exam_current_num + 1
# Goran
  if exam_consists[i] == GORAN[i % len(GORAN)]:
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