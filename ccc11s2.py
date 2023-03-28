
n = int(input())

st_responses = ""
answer = ""
for i in range(2*n):
  if i < n:
    st_responses = st_responses + input()
  else:
    answer = answer + input()

correctly = 0
for i in range(n):
  if st_responses[i] == answer[i]:
    correctly = correctly + 1

print(correctly)