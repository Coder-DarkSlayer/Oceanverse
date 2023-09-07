from math import pi # Importing pi from math module
def CircleArea(r): # Defining CircleArea function
    return round(pi*(r**2),2) # Returning area of circle with radius r

x = int(input("Enter the radius : ")) # Taking input
print(f"Area for circle with radius {x} is {CircleArea(x)}") # Printing output