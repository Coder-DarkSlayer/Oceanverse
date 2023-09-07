def prime(n): # takes n as an input
    for i in range(2,int(n/2)+1): # performing a loop till n/2
        if n%i == 0:
            return False # performing prime check even at any condition fail number isn t a prime
    return True

def primes(n): # taking a number as an input
    for i in range(2,n+1): # running loop for all numbers
        if prime(i) == True: # performing prime test for i
            print(i) # displaying numberds which passed the test

val = int(input("Enter a number: ")) #user innput for number of time to execute code

primes(val) # running the function