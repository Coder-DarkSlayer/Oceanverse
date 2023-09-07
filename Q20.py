from time import sleep # Importing sleep function from time module

def parabola(n,c): # n is the number of lines, c is the coefficient of x^2
    o =int(n/2) # o is the offset
    max = int(((o**2)*abs(c)/4)) # max is the maximum number of spaces
    if c >= 0: # checking if the coefficient is positive or negative
        for i in range(0,n):  # looping through the range
            var = int((((o-i)**2)*abs(c)/4)) # var is the number of spaces
            sleep(0.1) # sleep for 0.1 seconds
            print((var)*" "+ "*") # printing the star pattern
    else: # if the coefficient is negative
        for i in range(0,n): # looping through the range
            var = int((((o-i)**2)*abs(c)/4)) # var is the number of spaces
            sleep(0.1) # sleep for 0.1 seconds
            print((max-var)*" "+ "*") # printing the star pattern

n = int(input("Enter the number of lines : ")) # taking user input
c = int(input("Enter the curve : ")) # taking user input
parabola(n,c) # calling the function