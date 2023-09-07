l = [2,4,6,44,4,4,3,6,4,6,44,54,5579979,3567,2,4257,43435,41,343] #list to be sorted

def bubbleSort(lst): #bubble sort function
    x = len(lst) #length of the list
    for i in range(x): #iterate through the list
        for j in range(x): #iterate through the list
            if lst[i]<lst[j]: #if the element at i is less than the element at j
                temp = lst[i] #swap the elements
                lst[i] = lst[j] #swap the elements
                lst[j] = temp #swap the elements
    return lst #return the sorted list

if __name__ == "__main__": #driver code
    print(bubbleSort(l))