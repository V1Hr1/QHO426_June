#Definition of a new function - specifying what it does so it can be used later
def t_area():
  area = b*h*0.5
  print(area)

#Call the function to make it run
t_area()
t_area()
t_area()

#Parameter - data given or injected into a function

def t_area(b, h):
  area = b*h*0.5
  print(area)

#Call the function to make it run
t_area(2,8)
t_area(4,8)
t_area(7,12)

#Default parameter - value assumed by the parameter if no argument is given
def t_area(b=1, h=1):
  area = b*h*0.5
  print(area)

#Call the function to make it run
t_area()
t_area(4,8)
t_area(7)


#ddd
def t_area(b=1, h=1):
  area = b*h*0.5
  return area

def run():
#Call the function to make it run
  Total_area = t_area()+t_area(4,8)+t_area(7)
  print(Total_area)
  print(t_area(7,5))
run()