def matrixSum(m1,m2): # m1,m2 are 2D lists
    n = len(m1) # number of rows
    m3 = [] # empty list

    for i in range(n): # for each row
        x= [] # empty list
        for j in range(n): # for each column in row i 
            x.append(m1[i][j]+m2[i][j]) # add the two elements
        m3.append(x) # add the row to m3
    return m3 # return the matrix

# execution
print(matrixSum(
    [[1,2,3],[3,4,5],[5,6,7]],[[1,2,3],[3,4,5],[5,6,7]]
))