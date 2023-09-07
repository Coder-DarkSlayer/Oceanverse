def binSearch(l , f): # Binary search function
    high = len(l)-1 #high is the last index of the list
    low = 0 #low is the first index of the list
    mid = int(len(l)/2) #mid is the middle index of the list

    while low < high : #iterate through the list
        if f == l[mid]: #if the element is found
            return f"{f} is found at index {mid}." #return the element
        
        elif f > l[mid]: #if the element is greater than the middle element
            low = mid + 1 #low is the middle index
            mid = (low+high)//2  #mid is the middle index

        elif f < l[mid]: #if the element is less than the middle element
            high = mid -1 #high is the middle index
            mid = (low+high)//2  #mid is the middle index
        
    return f"{f} isn't present in list." #return the element
        
x = [1, 2, 4, 5, 5, 6, 7, 7, 8, 8, 9, 9, 41] #list to be searched
p = 25 #element to be searched

print(binSearch(x,p)) #calling binary search function