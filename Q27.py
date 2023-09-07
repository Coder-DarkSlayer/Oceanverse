def age(n): # n is the age
    if n < 18 :     # checking if the age is less than 18
        print("You're a Minor!") # printing the result
    elif n >=18 and n <= 65: # checking if the age is between 18 and 65
        print("You're an Adult.") # printing the result
    else: # if the age is greater than 65
        print("You're a senior citizen.") # printing the result

x = int(input("Enter your age : ")) # taking user input
age(x)  # calling the function