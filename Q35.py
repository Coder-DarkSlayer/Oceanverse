def fib(n): # n is a positive integer
    seq = [0,1] # list to store fibonacci sequence
    first = 0 # first term of fibonacci sequence
    second =1 # second term of fibonacci sequence
    i = 0 # counter variable
    while i < n-2: # loop to generate fibonacci sequence
        seq.append(first + second) # append next term to list
        first , second = second , first + second # update first and second term
        i+=1 # increment counter

    return seq[-1] # return nth term of fibonacci sequence

x = int(input("Enter a Integer : ")) # input
print(f"{x}th Fibonacci term is {fib(x)}") # output