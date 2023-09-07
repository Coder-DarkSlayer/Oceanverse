import csv # importing csv module
import numpy as np # importing numpy module
from scipy.signal import argrelextrema as arg # importing argrelextrema function from scipy.signal module
from datetime import datetime as d
initialBal , currBal = 100000 , 100000 # initial balance and current balance

"""
pip install scipy
pip install numpy
"""

with open("Sensex.csv" , 'r') as f: # opening Sensex.csv file in read mode
    iterator = csv.reader(f) # creating iterator
    headers = [] # creating empty list for headers
    headers = next(f) # storing headers in headers list
    
    data = [] # creating empty list for data
    dates = [] # creating empty list for dates
    for i in iterator: # iterating over iterator
        data.append(float(i[-1])) # appending data in data list
        dates.append(i[0]) # adding dates to list
    f.close() # closing the file

data = np.array(data) # converting data list into numpy array
o = 4 # order of local maxima and minima

# Get values of local maxima and minima
minIndices = (arg(data, np.less,order=o))[0].tolist() # getting indices of local minima
maxIndices = arg(data, np.greater,order=o)[0].tolist() # getting indices of local maxima

boughtOn = [] # creating empty list for boughtOn
soldOn = [] # creating empty list for soldOn

buyingSchedule = [[],[]] # list for storing purchase dates
buyingPrice = [[],[]] # list for storing purchase prices

for i in maxIndices: # looping for finding and arranging offers according to the date and prices
    for j in minIndices:
        if (d.strptime(dates[i],"%d-%B-%Y") > d.strptime(dates[j],"%d-%B-%Y")) and ((dates[i] not in buyingSchedule[1]) and (dates[j] not in buyingSchedule[0])):
            buyingSchedule[0].append(dates[j])
            buyingSchedule[1].append(dates[i])

            buyingPrice[0].append(data[j])
            buyingPrice[1].append(data[i])
            break

for i in range(int(len(buyingSchedule[0]))): # compounding the profit
    stocks  = currBal/buyingPrice[0][i] # purchasing stocks on minimum price
    currBal = stocks*buyingPrice[1][i] # selling stocks on maximum price

with open("Q43.txt" , "w") as f: # opening Q43.txt file in append mode
    for i in range(int(len(buyingSchedule[0]))): # writing the result in Q43.txt file
        f.writelines(f"\nStocks were bought on {buyingSchedule[0][i]} at price {buyingPrice[0][i]}.\nStocks were sold on {buyingSchedule[1][i]} at price {buyingPrice[1][i]}.")

    f.write(f"\nTotal balance after compounding is {round(currBal, 2)}.\n") # writing the result in Q43.txt file
    f.close() # closing the file

# printing the result
print(f"You Would've made maximum profit of {round((currBal - initialBal), 2)}.") # printing the result