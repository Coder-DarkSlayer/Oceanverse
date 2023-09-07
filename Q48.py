def WriteToFile(n): # n is the number of lines to be written
    l = [] # list to store the numbers
    for i in range(1,n+1):  # iterating over range 1 to n+1
        l.append(i) # appending i in l
    with open ("output.txt", "w") as f: # opening output.txt file in write mode
        for i in l: # iterating over l
            f.write(str(i)+'\n') # writing i in file
    f.close() # closing the file

n = int(input("Enter the number of lines to be written: ")) # taking input from user
WriteToFile(n) # calling WriteToFile function