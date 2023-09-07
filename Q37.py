from random import randint #importing random module

def bins(n):
    l = [] #making a box container
    for i in range(n):
        l.append([]) #adding n boxes in l

    empty = len(l) #counting empty boxes
    count = 0 #counting total balls

    while empty > 0: #looping until all boxes are filled
        x = randint(0,n-1) #randomly selecting a box
        if len(l[x]) == 0: #checking if the box is empty
            l[x].append(1) #adding a ball in the box
            empty -= 1 #decreasing empty box count
            count += 1 #increasing total ball count
        else:
            l[x].append(1) #adding a ball in the box
            count += 1 #increasing total ball count
    return count #returning total ball count

#taking input from user
val = int(input("Enter number of boxes: "))
print(f"Total balls: {bins(val)}") #printing total ball count