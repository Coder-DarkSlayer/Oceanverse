def Divisibility(n,d1,d2): # n is the number, d1 and d2 are the divisors
    if n %d1 == 0 and n %d2 ==0: # checking if n is divisible by both d1 and d2
        print(f"{n} is Divisible by both {d1} and {d2}") # printing the result
    else: # if n is not divisible by both d1 and d2
        print(f"{n} is not divisible by both {d1} and {d2}") # printing the result

# taking user input
x = int(input("Enter a number to check its divisibility : "))
y = int(input("Enter first divisor to check its divisibility : "))
z = int(input("Enter second divisor to check its divisibility : "))
# calling the function
Divisibility(x,y,z)