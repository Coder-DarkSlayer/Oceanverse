# Ceasar Cipher dictionary implementation
cipher = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j": 9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r": 17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25}

def encryptCeasar(obj,key): # encryption function
    obj = obj.lower() # lower case
    global cipher # access global dictionary
    res = "" # result string
    for i in obj: # iterate through string
        if i in cipher.keys(): # check if character is in dictionary
            temp = (cipher[i]+cipher[key]) % 26 # add key to character value
            res += list(cipher.keys())[list(cipher.values()).index(temp)] # add character to result string
    return res # return result string

def decryptCeasar(obj,key): # decryption function
    obj = obj.lower() # lower case
    global cipher # access global dictionary
    res = "" # result string
    for i in obj: # iterate through string
        if i in cipher.keys(): # check if character is in dictionary
            temp = (cipher[i]-cipher[key]) % 26 # subtract key from character value
            res += list(cipher.keys())[list(cipher.values()).index(temp)] # add character to result string
    return res # return result string

if __name__ == "__main__": # driver code
    x  = int(input("Enter 1 to encrypt and 2 to decrypt : "))

    if x == 1:
        val  = input("Enter string to encrypt : ")
        key = input("Enter encryption key : ")
        print(f"Encryped string is : {encryptCeasar(val,key)}\n")
    
    elif x == 2:
        val  = input("Enter string to decrypt : ")
        key = input("Enter decryption key : ")
        print(f"Decryped string is : {decryptCeasar(val,key)}\n")

    else:
        print("Invalid input")