# Advent of Code 2020 - Day 2 - Puzzle 2 Solution:

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

# Counters for valid / invalid passwords: 
total_ok = 0
total_not_ok = 0

# Condition (position 1, position 2, which letter) and password are consecutively derived for each line of the input file:
for k in range(0,n):
  line2 = out[k]
  j = 0
  for i in range(0,len(line2)):
    if line2[i] == '-':
      pos1 = int(line2[0:i])-1
      hyphen = i
    if line2[i] == ' ':
      pos2 = int(line2[hyphen+1:i])-1
      letter = line2[i+1]
      pwd = line2[i+4:len(line2)+1] 
      break
  
  # Check, if one of the positions contains the required letter while the second position does not. Number of valid / invalid passwords is increased accordingly: 
  print(f'{letter}, {pwd[pos1]}, {pwd[pos2]}'), 
  if pwd[pos1] == letter:
    if pwd[pos2] is not letter:
      total_ok = total_ok + 1
    elif pwd[pos2] == letter:
        total_not_ok = total_not_ok + 1
  elif pwd[pos1] is not letter:
    if pwd[pos2] == letter:
      total_ok = total_ok + 1
    else:
      total_not_ok = total_not_ok + 1

print(f'{total_ok} passwords are ok, while {total_not_ok} passwords are wrong.')
