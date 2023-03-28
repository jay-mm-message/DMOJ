
row = int(input())

t_total = 0
s_total = 0
for r in range(row):
    line = input()
    t_total = t_total + line.count('t')
    t_total = t_total + line.count('T')
    s_total = s_total + line.count('s')
    s_total = s_total + line.count('S')

if t_total > s_total:
    print('English')
elif s_total > t_total:
    print('French')
else:
    print('French')