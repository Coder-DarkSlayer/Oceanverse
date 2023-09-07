def star(n): # n is the number of lines
    for i in range(1,n+1): # looping through the range
        print((n-i)*" " + i*"*") # printing the star pattern

n = int(input("Enter the number of lines : ")) # taking user input
star(n) # calling the function