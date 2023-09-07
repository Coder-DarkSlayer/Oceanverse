def bin(res): # takes decimal number as input and returns binary number as output
    rem = 0 # remainder
    main = 0 # binary number
    x = 1 # power of 10
    while res>0: # looping till res is greater than 0
        rem = res%2 # calculating the remainder
        res = res//2 # dividing res by 2
        main+= rem*x # adding the remainder to the main variable
        x*=10 # increasing the power of 10

    return main # returning the binary number

# taking user input
x = int(input("Enter a number : "))
# calling the function
print(f"Binary valur of {x} is {bin(x)}.")