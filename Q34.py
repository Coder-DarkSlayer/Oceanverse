def fac(n): # n is a positive integer
    if n ==1 or n == 0: # base case
        return 1 
    elif n< 0: # error case
        return "Factorial of negative number doesn,t exist."
    else : # recursive case
        return n*fac(n-1) # recursive call
    
x = int(input("Enter a number : ")) # input
print(fac(x)) # output