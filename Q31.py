l = [] # Global list
def add(n): # n is the number
    global l # making l global
    for i in range (1, n+1): # looping from 1 to n
        l.append(i) # appending i to l list
    return l # returning the list

x = int(input("Enter a number : ")) # taking user input
print(add(x)) # calling the function