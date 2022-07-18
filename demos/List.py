#Declare an empty list
bleh = []
meh = list()
#Declare a non-empty list
yummy = ["Pizza", "Sarmale", "Ice Cream", "Musaka"]
#Print the list
print(yummy)
#Print a single item
print(yummy[2])
#Print some items
print(yummy[:2])
#Add elements to our list (exapand it) - adding at the end of the list
print(bleh)
bleh.append("Steak")
bleh.append("Salad")
bleh.append("Filet")
bleh.append("Cake")
print(bleh)
#Add multiple items to a list
for i in range (2):
  bleh.append("Salad2")
print(bleh)
bleh.extend(["Soup", "Caramel", "fish"])
print(bleh)
#Insert items at speciffic positions on the list
bleh.insert(1, "Cabbage")
bleh.insert(4, "Mushed Peas")
print(bleh)
#Remove items from the list
if "Caramel" in bleh:
  bleh.remove("Caramel")
if "Steak" in bleh:
  bleh.remove("Steak")
print(bleh)
#Remove item by index
x = bleh.pop(1)
print(bleh)
print(x*8)
#Alternative way to delete an item by Index
del bleh[2]
print(bleh)
#Extending list with another lkst
yummy.extend(bleh)
print(yummy)
print(bleh)
#Mutating a list
yummy[4] = "Hamburger"
yummy[1] = 67894
print(yummy)
#Check a lkst for particular data type
lista = ["Fred", 56, True, "Piotor", -4.8, "Ham", 89, False]
for item in lista:
  if isinstance(item, str):
    print(item)
