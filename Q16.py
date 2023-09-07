def counter(s): # s is a string
    vowel = ["a","e","i","o","u"] # list of vowels
    v = 0 # counter for vowels
    c = 0 # counter for consonants
    for i in range(0,len(s)): # looping through the string
        if s[i].lower() in vowel: # checking if the character is a vowel
            v+=1 # if vowel, increment the counter
        else: # if not vowel, increment the counter
            c+=1 # if consonant, increment the counter
    print(f"Following word has {v} Vowels, and {c} Consonants.") # display the result

x = (input("Enter a String : ")) # taking user input
counter(x) # calling the function