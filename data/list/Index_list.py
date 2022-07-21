def movements():
  return ["Move forward", 10, "Move back", 5, "Mowve left", 3, "move right", 1]

def run():
  print("Moving....")
  micky_mouse = movements()
  for i in range(0, len(micky_mouse), 2):
    print(f"{micky_mouse[i]} for {micky_mouse[i+1]} steps")

run()