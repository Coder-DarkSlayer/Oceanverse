def prime(n): #takes n as an input
    for i in range(2,int(n/2)+1): # runs loop till n/2 to check for divisibility
        if n%i == 0: # if remainder is 0 number isn't prime
            print("Given Number is not Prime.")
            return False #ends the function
    print("Given number is Prime.") #else number is prime
    return True #ends the function

val = int(input("Enter a number: ")) #user innput for number of time to execute code

prime(val)