def ReadFile(): # Read the file and print the content
    with open("output.txt" , "r") as f : # Open the file in read mode
        x = f.read().splitlines() # Read the lines of the file
    for i in x: # Iterate through the lines
        print(i) # Print the lines
    f.close() # close file

ReadFile() # Call the function