def sum(arr): # sum of all elements in list
    res = 0 # result
    for i in arr: # for each element in list
        res += i # add to result
    return res # return result

def positive(arr): # largest positive sum
    x = True # flag
    temp = 0 # temporary variable
    for i in arr: # we check each element in list
        if i < 0: # if any element is negative
            x = False # flag is false
            break # break loop
        elif i > temp: # if element is greater than temporary variable
            temp = i # assign element to temporary variable
    return temp,x # return temporary variable and flag

def negative(arr): # largest negative sum
    x = True # flag
    temp = arr[0]   # temporary variable
    for i in arr: # we check each element in list
        if i > 0: # if any element is positive
            x = False # flag is false
            break # break loop
        elif i > temp: # if element is greater than temporary variable
            temp = i # assign element to temporary variable
    return temp,x # return temporary variable and flag

def contiguousSum(arr): # function to find largest contiguous sum
    if positive(arr)[1]: # if all elements are positive
        return sum(arr) # return sum of all elements
    
    elif negative(arr)[1]: # if all elements are negative
        return negative(arr)[0] # return largest negative element
    
    else: # if both positive and negative elements are present
        currSum = 0 # current sum
        maxSum = 0 # maximum sum
        for i in arr: # for each element in list
            currSum += i # add element to current sum
            if currSum > maxSum: # if current sum is greater than maximum sum
                maxSum = currSum # assign current sum to maximum sum
            
            elif currSum < 0: # if current sum is less than 0
                currSum = 0 # assign 0 to current sum

        return maxSum  # return maximum sum
        
# Driver Code
if __name__ == "__main__":

    z = input("Enter list elements with \",\" as seperator to find largest contiguous sum : ")
    z = z.split(",")
    x= []
    for i in z:
        x.append(int(i))

    if z == []:
        print(f"List is empty!")
    else:
        print(f"Largest contiguous sum is {contiguousSum(x)}")