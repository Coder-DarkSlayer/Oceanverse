def square(n): # n is the number of lines
    for i in range(1,n+1):  # looping through the range
        print(i**2) # printing the square of the number

n = int(input("Enter the number of lines : ")) # taking user input
square(n) # calling the function