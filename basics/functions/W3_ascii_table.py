print("Program started!")
print("Please enter a char!")
x = abs(int(input()))
if x in range(32, 127):
  print(f"The char represented by the ASCII Code {x} is {chr(x)}") 

print("The prog ended")