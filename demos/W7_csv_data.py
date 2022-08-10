import csv
import matplotlib.pyplot as plt

def gather_data(n=1):
  with open("june_data.csv", "w") as file:
    csv_writer = csv.writer(file)
    for i in range (n):
      h = float(input("Enter height: "))
      w = float(input("Enter weight: "))
      csv_writer.writerow([h,w])

def retrieve_data():
  with open("june_data.csv") as file:
    hs = []
    ws = []
    csv_reader = csv.reader(file)
    for row in csv_reader:
      hs.append(float(row[0]))
      ws.append(float(row[1])) 
  return hs, ws

def graphs():
  x, y = retrieve_data()
  plt.plot(x, y, "ro-")
  plt.show()

graphs()