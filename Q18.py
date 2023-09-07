def fib(n): # n is the number of lines
    seq = [0,1] # list of first two numbers
    for i in range(0,n-1): # looping through the range
        seq.append((seq[i])+seq[i+1]) # appending the sum of last two numbers
    
    for i in seq: # looping through the list
        print(i,end = ", ") # printing the number

n = int(input("Enter the number of lines : ")) # taking user input
fib(n) # calling the function