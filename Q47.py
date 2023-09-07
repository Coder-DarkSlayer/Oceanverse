def transposeMatrix(m): # m is a matrix
    res = [] # empty list
    n = len(m) # number of rows

    for i in range(n): # for each row
        x= [] # create empty list
        for j in range(n): # for each column in row i
            x.append(m[j][i]) # add the element to x
        res.append(x) # add the row to res
    return res # return the matrix

def product(l1,l2): # l1,l2 are lists of equal length
    l3 = [] # empty list
    for i in range(len(l1)): # for each element in l1
        l3.append(l2[i]*l1[i]) # add the product to l3
    total = 0 # initialize total
    for i in l3: # for each element in l3
        total += i # add the element to total
    return total # return the total

def matrixProduct(m1,m2): # m1,m2 are 2D lists
    m2 = transposeMatrix(m2) # transpose m2
    m3 = [] # empty list
       
    for j in m1: # for each row in m1
        x = [] # empty list
        for k in m2: # for each row in m2
            x.append(product(j,k)) # add the product to x
            
        m3.append(x) # add the row to m3

    return m3 # return the matrix

# execution
print(matrixProduct([[1,2,3],[3,4,5],[5,6,7]],[[1,2,3],[3,4,5],[5,6,7]]))