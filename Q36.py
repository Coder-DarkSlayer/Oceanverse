from random import randint #importing randint function from random module

def bins(n):
    l = [] #making a box container
    for i in range(n):
        l.append([]) #adding n boxes in l

    for i in range(n):
        x = randint(0,n-1) #calculating random index
        #let stars denote balls
        l[x].append("*") #adding ball in random box

    return l

val = int(input("Enter total number of balls : ")) #input
boxes = bins(val) #calling bins function

j = 0
for i in boxes: #finding maximun number of balls
    if len(i) > j:
        j = len(i)

print(j) #output