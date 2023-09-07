def AP(a,d,f): # taking first , max possible and common diffrence terms
    while a <=f: # running loop till first term reachers max possible term
        print(a) # displaying the term
        a+=d # incrementing the value

#taking respective inputs
x = int(input("Enter first term : "))
y = int(input("Enter Common difference term : "))
z = int(input("Enter Maximum limit term : "))

#excuting the code
AP(x,y,z)