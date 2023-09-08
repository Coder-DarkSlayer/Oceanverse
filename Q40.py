def spiralPattern(n): # prints the pattern
    count = 0 # count the number of characters printed
    i = 1 # number of characters to be printed

    res = "" # store result
    while count <= n : # loop until n characters are printed
        if i%2 != 0: # if i is odd
            if count + 2*i > n: # if current iteration exceeds n
                res += "R"*i + "U"*(n - count - i) # add only R and U till n
                break
            elif count + i > n: # if current iteration exceeds n
                res += "R"*(n - count) # add only R till n
                break
            else:
                res += "R"*i + "U"*i # add R and U alternatively
                count+=2*i

        else: # if i is even
            if count + 2*i > n: # if current iteration exceeds n
                res += "L"*i + "D"*(n - count - i) # add only L and D till n
                break
            elif count + i > n: # if current iteration exceeds n
                res += "L"*(n - count) # add only L till n
                break
            else:
                res += "L"*i + "D"*i # add L and D alternatively
                count+=2*i # increment count by 2*i

        i+=1   # increment i
    return res # return result with n letters

x = int(input("Enter steps in the spiral : ")) # input
print(spiralPattern(x)) # printing result