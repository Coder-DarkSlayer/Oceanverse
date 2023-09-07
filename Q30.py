def gcd(a,b,c = 0): # gcd function take two values and C is for counting total times function is called
    if a > b: # checking if a is greater than b
        if b == 0: # checking if b is zero
            return a, c # if b is zero return a and c
        elif a == b: # checking if a and b are equal
            return b,c # if numbers are equal return any of two
        else:
            return gcd(b,a%b,c+1) # if not return gcd of b and a modulo b
    else:
        if a == 0: # checking if a is zero
            return b,c # if a is zero return b and c
        elif b == a: # checking if a and b are equal
            return b,c # if numbers are equal return any of two
        else:
            return gcd(a,b%a,c+1) # if not return gcd of b and a modulo b

def func_1(k):
    min = 10**(k-1) #making minimum value for k digit
    max = 10**(k) #making maximum value consisting k digits
    count = 0 # counter for steps

    for i in range(min,max): #running loop twice to create a n*n array
        for j in range(min,max):
            temp = gcd(i,j)[1]
        
            if temp > count: # putting maimum value in count
                count,res1,res2 = temp,i,j # storing the values of i and j in res1 and res2

    return res1,res2,count,gcd(res1,res2)[0] #returning the result

# Executing the code

val = int(input("Enter number of digits to calculate GCD for : ")) #taking user input
y = func_1(val) #calling the function
print(f"GCD of {y[0]} and {y[1]} take maximum steps i.e. {y[2]} and their GCD is {y[3]}") #printing the result