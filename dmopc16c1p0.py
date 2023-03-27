unit = int(input())
extra_cheesiness = int(input())

if unit == 3 and extra_cheesiness >= 95:
    print('C.C. is absolutely satisfied with her pizza.')
elif unit == 1 and extra_cheesiness <= 50:
    print('C.C. is fairly satisfied with her pizza.')
else:
    print('C.C. is very satisfied with her pizza.')