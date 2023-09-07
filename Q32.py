from random import randint # importing randint from random module
def add(n): # n is the number
    l=[] # local list
    for i in range(n): # looping from 0 to n-1
        l.append(randint(1,1001)) # appending random number between 1 and 1000
    return l # returning the list

x = int(input("Enter amount of integers to append in list : ")) # taking user input
print(add(x)) # calling the function