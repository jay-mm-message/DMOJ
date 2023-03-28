
# B: parking_on_both_yesterday_and_today
# Y: parking_record_of_yesterday
# T: parking_record_of_today
# Total: parking_space_total
Total = int(input())
Y = input()
T = input()
B = 0
for i in range(Total):
    if Y[i] == 'C' and T[i] == 'C':
        B = B + 1

print(B)