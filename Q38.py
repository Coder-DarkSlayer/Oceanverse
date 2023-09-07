def is_even(n): # n is a positive integer
    if n%2 == 0: #if n is even
        return True #return True
    else: #if n is odd
        return False
    
x = int(input("Enter a Integer : ")) #input
print(is_even(x))   #output