seq = input("Please enter a seq!")
marker = input("Please enter a marker!")
pos1 = 99
pos2 = 99

for i in range(0, len(seq)):
  if(seq[i] == marker):
    if pos1 == -1:
      pos1 = i
    else:
      pos2 = i

print(f"8The distance between the markers is {pos2-pos1-1}")
  