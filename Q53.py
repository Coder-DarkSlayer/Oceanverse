def addList(l1,l2,l3): # function to add lists and the pivot
    l1.append(l2) #appending pivot to the list
    for i in l3: #iterating through the list
        l1.append(i) #appending the elements of the list to the list
    return l1   #returning the list

def quickSort(lst):
    if len(lst) == 1 or len(lst) == 0: #if list has emptied or listhas one element return it
        return lst #return the list
    else:
        pivot = lst.pop(-1) #choosing last element of list as pivot
        last = [] #empty list
        i = 0 #initializing i
        while i < len(lst): #running loop for elements in the list
            if lst[i] > pivot: #if the element is greater than pivot
                last.append(lst.pop(i)) #append the element to the last list
            else: #if the element is less than pivot
                i+=1 #increment i
                
        return addList(quickSort(lst),pivot,quickSort(last)) # calling add function

x = [1,44,55,2,66,3,55,46,46,34,95,9,47,45,37] #list to be sorted

if __name__ == '__main__': #driver code
    print(quickSort(x))