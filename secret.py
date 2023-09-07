def textstrip(filename): # This function is given to you
    '''This takes the file and converts it to a string with all the spaces and other
    special characters removed. What remains is only the lower case letters,
    retain only the lowercase letters!
    ''' 
    with open(filename,'r') as f: # This opens the file in read mode
        s = f.read() # This reads the contents of the file into a string
        f.close()
        res = "" # This is the string that we will return
    for i in s: # For each character in the string
        if i.isalpha() and i.islower(): # If it is a lowercase letter
            res+=i # Add it to the result

    return res # Return the result

def letter_distribution(s): # This function is given to you
    '''Consider the string s which comprises of only lowercase letters. Count
    the number of occurrences of each letter and return a dictionary'''
    d = {} # This is the dictionary that we will return
    for i in s: # For each character in the string
        if i in d.keys(): # If the character is already in the dictionary
            d[i]+=1 # Increment the count
        else: # If the character is not in the dictionary
            d[i]=1 # Add it to the dictionary with a count of 1
    return d # Return the dictionary

def substitution_encrypt(s,d): # This function is given to you
    '''encrypt the contents of s by using the dictionary d which comprises of
    the substitutions for the 26 letters. Return the resulting string'''
    res = "" # This is the string that we will return
    for i in s: # For each character in the string
        res+=d[i] # Add the substitution to the result
    return res # Return the result

def substitution_decrypt(s,d): # This function is given to you
    '''decrypt the contents of s by using the dictionary d which comprises of
    the substitutions for the 26 letters. Return the resulting string'''

    res  = "" # This is the string that we will return
    for k in s: # For each character in the string
        res+=list(d.keys())[list(d.values()).index(k)]

    return res # Return the result

def cryptanalyse_substitution(s): # This function is given to you
    '''Given that the string s is given to us and it is known that it was
    encrypted using some substitution cipher, predict the d'''

    rank = ['e','t','a','o','i','n','s','h','r','d','l','c','u','m','w','f','g','y','p','b','v','k','j','x','q','z'] # This is the rank of the letters in English
    letters = set(s) # This is the set of letters in the string s
    d = {} # This is the dictionary that we will return
    while len(letters)>0: # While there are still letters left
        temp = max(letters,key = s.count) # Find the most frequent letter
        d[rank[0]] = temp # Add it to the dictionary
        letters.remove(temp) # Remove it from the set
        rank.pop(0)      # Remove it from the rank
    
    return d # Return the dictionary

def vigenere_encrypt(s,password): # This function is given to you
    '''Encrypt the string s based on the password the vigenere cipher way and
    return the resulting string'''
    
    cipher = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j": 9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r": 17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25}
    i = 0 # This is the index of the password
    res = "" # This is the string that we will return
    if len(s)> len(password): # If the length of the string is greater than the length of the password
        while len(password)<len(s): # While the length of the password is less than the length of the string
            password+=password[i] # Add the ith character of the password to the end of the password
            i+=1 # Increment i
    else: # If the length of the string is less than the length of the password
        password = password[:len(s)] # Truncate the password to the length of the string

    for i in range(len(s)): # For each character in the string
        temp = (cipher[s[i]]+cipher[password[i]])%26 # Add the two characters and take the mod 26
        res += list(cipher.keys())[list(cipher.values()).index(temp)] # Add the character corresponding to the value to the result
    return res # Return the result

def vigenere_decrypt(s,password): # This function is given to you
    '''Decrypt the string s based on the password the vigenere cipher way and
    return the resulting string'''
    cipher = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j": 9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r": 17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25}
    i = 0 
    res = "" # This is the string that we will return
    if len(s)> len(password): # If the length of the string is greater than the length of the password
        while len(password)<len(s): # While the length of the password is less than the length of the string
            password+=password[i] # Add the ith character of the password to the end of the password
            i+=1 # Increment i
    else:
        password = password[:len(s)] # Truncate the password to the length of the string

    for i in range(len(s)): # For each character in the string
        temp = (cipher[s[i]]-cipher[password[i]])%26    # Subtract the two characters and take the mod 26
        res += list(cipher.keys())[list(cipher.values()).index(temp)] # Add the character corresponding to the value to the result
 
    return res # Return the result

def rotate_compare(s,r): # This function is given to you
    '''This rotates the string s by r places and compares s(0) with s(r) and
    returns the proportion of collisions'''
    temp = s[r:]+s[:r] # This is the rotated string
    count  = 0 # This is the number of collisions
    for i in range(len(s)): # For each character in the string
        if s[i] == temp[i]: # If the characters are the same
            count += 1 # Increment the count
    return count # Return the count

def cryptanalyse_vigenere_afterlength(s,k): # This function is given to you
    '''Given the string s which is known to be vigenere encrypted with a
    password of length k, find out what is the password'''
    cipher = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j": 9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r": 17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25}

    key = "" # This is the string that we will return
    for i in range(k): # For each character in the password
        temp = "" # This is the string that will store the ith characters of the string
        for j in range((len(s)//k)+1): # For each block of length k
            try:
                temp += s[(k*j)+i] # Add the ith character of the block to the string

            except IndexError: # If the index is out of bounds
                pass
        common = (cipher[max(set(temp), key = temp.count)]-4)%26 # Find the most common character and subtract e from it
        key += list(cipher.keys())[list(cipher.values()).index(common)] # Add the character corresponding to the value to the result
    return key # Return the result

def cryptanalyse_vigenere_findlength(s): # This function is given to you
    '''Given just the string s, find out the length of the password using which
    some text has resulted in the string s. We just need to return the number 
    k'''
    collisions = [] # This is the list of collision frequencies
    for i in range(1,len(s)+1): # For each possible length of the password
        collisions.append((rotate_compare(s,i))/len(s)) # Add the collision frequency to the list
    for i in range(len(collisions)): # For each collision frequency
        if collisions[i]>0.055: # If the collision frequency is greater than 0.055
            return i+1 # Return the index of the first collision frequency that is greater than 0.055
        
def cryptanalyse_vigenere(s): # This function is given to you
    '''Given the string s cryptanalyse vigenere, output the password as well as
    the plaintext'''
    k = cryptanalyse_vigenere_findlength(s) # Find the length of the password
    p = cryptanalyse_vigenere_afterlength(s,k) # Find the password
    d = vigenere_decrypt(s,p) # Decrypt the string
    print(f"Password : {p}\n\nPlaintext : {d}") # Print the password and the plaintext