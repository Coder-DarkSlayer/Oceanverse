def pattern(n): # prints the pattern
    count = 0 # count the number of characters printed
    i = 1 # number of characters to be printed

    res = "" # store result
    while count <= n : # loop until n characters are printed
        if i%2 != 0: # if i is odd
            res += "R"*i + "U"*i # add R and U alternatively
        else: # if i is even
            res += "L"*i + "D"*i # add L and D alternatively
        count += i*2 # increment count
        i+=1   # increment i
    return res[:n] # return result with n letters

x = pattern(1000000) # running function
print(x) # printing result