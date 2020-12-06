# Advent of Code 2020 - Day 2 - Puzzle 1 Solution:

f = open("Day2_Puzzle_Input.txt", "r")

# Content of Day2_Puzzle_Input.txt is written to out[]:
out = []
n = 0
while True:
  line = f.readline()
  n = n + 1
  if not line:
    n = n - 1
    break;
  out.append(line.strip())

# Condition (min, max, which letter) and password are conescutively derived for each line of the input file:
total_ok = 0
total_not_ok = 0
for k in range(0,n):
  line2 = out[k]
  j = 0
  for i in range(0,len(line2)):
    if line2[i] == '-':
      min = line2[0:i]
      hyphen = i
    if line2[i] == ' ':
      max = line2[hyphen+1:i]
      letter = line2[i+1]
      pwd = line2[i+4:len(line2)+1] 
      break
  
  # Check, if the condition for the password is fulfilled. Number of wrong, respectively correct passwords is increased accordingly: 
  count = 0
  for l in range(0,len(pwd)):
    if pwd[l] == letter:
      count = count + 1
  if count < int(min) or count > int(max):
    total_not_ok = total_not_ok + 1
  else:
    total_ok = total_ok + 1

print(f'{total_ok} passwords are ok, while {total_not_ok} passwords are wrong.')
