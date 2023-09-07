def factorial(n): # n is the number of lines
    if n == 1 or n == 0: # checking if n is 1 or 0
        return 1 # returning 1
    else: # if n is not 1 or 0
        return n*factorial(n-1) # returning the factorial of n

n = int(input("Enter the number for finding factorail : ")) # taking user input
print(factorial(n)) # calling the function