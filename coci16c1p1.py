# M: Total megabytes
# N: Number of days spent

M = int(input())
N = int(input())

total_remain = M * ( N + 1 )
for i in range(N):
    spent_value = int(input())
    total_remain = total_remain - spent_value
print(total_remain)