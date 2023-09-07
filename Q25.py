def leapYear(n): # n is the year
    if n%4 == 0: # checking if the year is divisible by 4
        if n%100 == 0: # checking if the year is divisible by 100
            if n%400 ==0: # checking if the year is divisible by 400
                print(f"{n} is a leap Year.") # printing the result
            else: # if the year is not divisible by 400 but divisible by 100
                print(f"{n} is not a leap year.") # printing the result
        else: # if the year is not divisible by 100 but divisible by 4
            print(f"{n} is a leap Year.") # printing the result
    else: # if the year is not divisible by 4
        print(f"{n} is not a leap Year.") # printing the result

y = int(input("Enter year to check if it's leap : ")) # taking user input

leapYear(y) # calling the function