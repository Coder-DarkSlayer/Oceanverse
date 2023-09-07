def table(n,i = 1 , j = 10): # takes customized input but general case from 1 to 10
    for k in range(i,j+1): #runs loop from i to j
        print(f"{n} x {k} = {k*n}") # prints the table

val = int(input("Enter a number: ")) #user innput for number of time to execute code

table(val)