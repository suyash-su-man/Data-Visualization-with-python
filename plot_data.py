import matplotlib.pyplot as plt
# Part 1
import csv

x=[]
y=[]
with open('example.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))
plt.plot(x,y,label = 'Loaded from file!')        

# Part 2
import numpy as np
x,y = np.loadtxt('example.txt',delimiter = ',',unpack = True)
plt.plot(x,y,label = 'Loaded from file!')        

# part 3 Getting data from internet

stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
source_code = urllib.request.urlopen(stock_price_url).read


plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot demonstration')
plt.legend()
plt.show()