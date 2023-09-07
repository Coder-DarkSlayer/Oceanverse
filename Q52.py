def listMerger(l1, l2): # l1 and l2 are sorted lists
    l3 = [] #empty list
    x = len(l1)+len(l2) #length of the list
    while x >= len(l3): #iterate through the list
        if len(l1) == 0 and len(l2) == 0: #if both the lists are empty
            return l3 #return the list
        elif len(l2) == 0: #if the second list is empty
            l3.append(l1.pop(0)) #append the first element of the first list to the third list
        elif len(l1) == 0: #if the first list is empty
            l3.append(l2.pop(0))    #append the first element of the second list to the third list
        elif l1[0] > l2[0]: #if the first element of the first list is greater than the first element of the second list
            l3.append(l2.pop(0)) #append the first element of the second list to the third list
        else: #if the first element of the first list is less than the first element of the second list
            l3.append(l1.pop(0)) #append the first element of the first list to the third list


def mergeSort(l): #merge sort function
    if len(l) == 1: #if the length of the list is 1
        return l #return the list
    else: #if the length of the list is not 1
        n = int(len(l)/2) #find the middle element
        first = l[:n] #first half of the list
        last = l[n:] #second half of the list
        return listMerger(mergeSort(first), mergeSort(last)) #return the merged list


x = [1, 5, 7, 8, 9, 41, 0, 7] #list to be sorted
if __name__ == '__main__': #driver code
    print(mergeSort(x))
