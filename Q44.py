# Correlation can be measured on a scale from -1 to 1:

# A positive correlation closer to 1 indicates a strong positive relationship, meaning that as one variable increases, the other tends to increase proportionally.
# A negative correlation closer to -1 indicates a strong negative relationship, meaning that as one variable increases, the other tends to decrease proportionally.
# A correlation close to 0 suggests a weak or no linear relationship between the variables.

import csv # importing csv module
import matplotlib.pyplot as plt # importing matplotlib.pyplot module
import numpy as np # importing numpy module
from statistics import median , mean , mode # importing median , mean , mode function from statistics module

inch_to_metre = 0.0254 # 1 inch = 0.0254 metre
pound_to_kg = 0.453592 # 1 pound = 0.453592 kg

with open("HeightWeight.csv" , "r") as f: # opening HeightWeight.csv file in read mode
    iter = csv.reader(f) # creating iterator
    header =[] # creating empty list for headers
    header = next(f) # storing headers in header list
    data = [] # creating empty list for data
    for i in iter: # iterating over iterator
        data.append((float(i[1]),float(i[2]))) # appending data in data list
    f.close() # closing the file

bmidata = []
heightData = []
weightData = []

for i in data: # iterating over data list   
    bmi = (i[1]*pound_to_kg)/((i[0]*inch_to_metre)**2) # calculating bmi
    height = i[0]*inch_to_metre # calculating height
    weight = i[1]*pound_to_kg # calculating weight

    bmidata.append(bmi) # appending bmi in bmidata list
    heightData.append(height) # appending height in heightData list
    weightData.append(weight) # appending weight in weightData list

x = np.array([median(bmidata),median(weightData)]) # calculating median of data list
y = np.array([mean(bmidata),mean(weightData)]) # calculating mean of data list
z = np.array([mode(bmidata),mode(weightData)]) # calculating mode of data list

X = np.array(bmidata) # converting bmidata list into numpy array
Y = np.array(weightData) # converting heightData list into numpy array

bavg = np.average(bmidata) # calculating average of heightData list
wavg = np.average(weightData) # calculating average of weightData list

h = [0,2*bavg] # creating list for plotting horizontal line
v = [0,2*wavg] # creating list for plotting vertical line

cef = np.corrcoef(bmidata,weightData)[0][1]

plt.xlabel("Bmi (Kg/m²)")
plt.ylabel("Weight (Kg)")
plt.title(f"Plot\nCorrelation {round(cef,3)}")


plt.scatter(X,Y,s=0.1) # plotting scatter plot
plt.scatter(x[0],x[1],color="red",s=10) # plotting median point])
plt.scatter(y[0],y[1],color="black",s=10) # plotting median point])
plt.scatter(z[0],z[1],color="orange",s=10) # plotting median point])

plt.plot(h,v,color="green") # plotting horizontal and vertical line

plt.legend(["Data","Median","Mean","Mode"]) # adding legend

plt.show() # showing the plot