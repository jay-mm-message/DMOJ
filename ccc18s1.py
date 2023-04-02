
village_num = int(input())

village_position = list()
while village_num > 0:
  village_num = village_num - 1
  village_position.append(int(input()))

village_position = sorted(village_position)

# print(village_position)

v = village_position
neighborhoob_information = list()
for i in range(1, len(village_position) - 1, 1):
  neighborhoob = (v[i] - v[i-1]) / 2 + (v[i+1] - v[i])/2
  neighborhoob_information.append(neighborhoob)

# print(neighborhoob_information)

min_neighborhood = 0
min = min_neighborhood
info = neighborhoob_information
for i in range(len(info)):
  if i == 0:
    min = info[i]
  else:
    if min > info[i]:
      min = info[i]
print(min)
