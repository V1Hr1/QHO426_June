while True:
  print("Please, choose one of the options: \n1-Nice message\n2-Area of Rectangle\n3-Area of Triangle\n4-Times table\n5-exit")
  opt = int(input())
  if opt==1:
    print("You do not smell so bead today")
  elif opt==2:
    h=float(input("Enter height"))    
    w=float(input("Enter width")) 
    print(f"The area is {h*w}cm^2")
  elif opt==3:
    h=float(input("Enter height"))    
    b=float(input("Enter base")) 
    print(f"The area is {h*b*0.5}cm^2")
  elif opt==4:
    n=int(input("Enter whole num"))   
    for i in range(1,11):
      print(f"{h}x{i}={n*i}")
    print("That's all folks")
  elif opt==5:
    break
  else:
    print("WHOOPSY! No such option. Try again")