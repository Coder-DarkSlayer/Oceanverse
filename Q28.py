def grade(a,b,c,d,e): # a,b,c,d,e are the marks in 5 subjects
    n = (a+b+c+d+e)/5 # calculating the average
    if n >= 90: # checking if the average is greater than or equal to 90
        print("A Grade.") # printing the result
    elif n < 90 and n >= 80: # checking if the average is between 80 and 90
        print("B Grade.") # printing the result
    elif n < 80 and n >= 70: # checking if the average is between 70 and 80
        print("C Grade.") # printing the result
    elif n < 70 and n >= 60: # checking if the average is between 60 and 70
        print("D Grade.") # printing the result
    else: # if the average is less than 60  
        print("F Grade.") # printing the result

# taking user input
q = int(input("Enter Score in Subject 1 : "))
w = int(input("Enter Score in Subject 2 : "))
e = int(input("Enter Score in Subject 3 : "))
r = int(input("Enter Score in Subject 4 : "))
t = int(input("Enter Score in Subject 5 : "))

grade(q,w,e,r,t) # calling the function