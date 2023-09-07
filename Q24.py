def converter(t,p): # t = temperature, p = scale
    if p.upper() == "F": # if the scale is F then convert to C
        c =(t - 32)/1.8 # formula for conversion
        return str(round(c,3)) + " °C" # return the result
    else: # if the scale is C then convert to F
        f =( t*1.8)+ 32 # formula for conversion
        return str(round(f,3)) + " °F" # return the result

x = int(input("Enter the temperature : ")) # taking user input
y = input("Enter the Scale : ") # taking user input

print(converter(x,y)) # calling the functions