def func(n): # n is the number
    if n > 0: # checking if the number is positive or negative
        print("Number is positive.") # printing the result
    elif n < 0: # checking if the number is positive or negative
        print("Number is Negative") # printing the result
    else: # if the number is zero
        print("Number is zero.") # printing the result

x = int(input("Enter a Number : ")) # taking user input
func(x) # calling the function