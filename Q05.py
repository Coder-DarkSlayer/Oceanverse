def odd_even(n): #takes a number
    if n % 2 == 0: # if remainder after division with 2 is 0 it is even
        print("Given number is even")
    else: # if condition is not satisfied
        print("Given number is odd")

i = int(input("Enter a number : ")) # taking input from user

odd_even(i) #executing the function