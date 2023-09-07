def palindrome(s): # s is a string
    for i in range(0, int(len(s)/2)+ 1): # looping through the string
        if s[len(s)-1-i] == s[i]: # checking if the characters are equal
            continue # if equal, continue
        else: # if not equal, display this message
            print("Given string is not a Palindrome.")
            return 0 # end the function
    print("Given string is Palindrome.")

x = (input("Enter a String : ")) # taking user input
palindrome(x) # calling the function