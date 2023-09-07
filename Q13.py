def interperse(s1,s2): # takes two strings as an input
    result = "" # empty string to store the result
    if len(s1) != len(s2):# checking if the length of the strings are equal
        print("Length of strings are not equal.")# if not equal, display this message
    else:# if equal, then proceed
        for i in range(0 , len(s1)): # looping through the length of the string
            result += (s1[i]+ s2[i]) # adding the characters of the strings to the result
        print(result) # displaying the result

# taking user input
x = (input("Enter first String : "))
y = (input("Enter second String : "))

interperse(x,y) # calling the function and displaying the result