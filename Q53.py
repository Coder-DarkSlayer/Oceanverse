def partition(lst , start , end): # partition function
    pivot = lst[end] # pivot is the last element of the list

    while start < end: # while start is less than end
        if lst[start]>pivot: # if the element at start is greater than pivot
            lst.insert(end , lst.pop(start)) # insert the element at end and pop the element at start
            end -= 1 # decrement end
        else: # if the element at start is less than pivot
            start += 1 # increment start
    return end # return end

def quickSort(lst, start , end): # quick sort function
    if start < end: # if start is less than end
        temp = partition(lst , start , end) # temp is the partition function
        quickSort(lst , start, temp -1) # recursive call to quick sort function
        quickSort(lst , temp + 1 , end) # recursive call to quick sort function

if __name__ == '__main__': #driver code
    x = [1,44,55,2,66,3,55,46,46,34,95,9,47,45,37] #list to be sorted
    print(quickSort(x,0,len(x)-1))