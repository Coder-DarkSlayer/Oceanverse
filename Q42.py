def FindMax(l): # l is a list
    max = 0 # max is a integer
    for i in l: # i is a integer
        if max < i : # max is less than i
            max = i
        else:
            continue
    return max

l = [35,7,35,47,7,57,4,74,84,34,84,5,58] # l is a list

print(f"Max integer in Given list is {FindMax(l)}") # print max integer in given list