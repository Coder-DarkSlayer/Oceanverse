def reverse(s): # s is a string
    x = "" # empty string to store the result
    for i in range(len(s)-1,-1,-1): # looping through the string in reverse order
        x += s[i] # adding the characters to the result
    return x # returning the result

x = (input("Enter a String : ")) # taking user input
print(reverse(x)) # calling the function and displaying the result