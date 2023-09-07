angle = 90 # initial angle
coordinates = [(1,1)] # initial coordinates

def right(theta):  # function to turn right
    theta -= 90  # subtract 90 degrees from the current angle
    theta = theta%360  # make sure the angle is between 0 and 360
    return theta 

def left(theta): # function to turn left 
    theta += 90 # add 90 degrees to the current angle
    theta = theta%360  # make sure the angle is between 0 and 360
    return theta 

def forward(size,angle): # function to move forward and update
    global coordinates  # the coordinates
    x = coordinates[-1][0]  # get the current x coordinate
    y = coordinates[-1][1]  # get the current y coordinate
    if angle == 0:  # if the angle is 0, move right
        coordinates.append((x+size , y)) 
    
    elif angle == 90: # if the angle is 90, move up
        coordinates.append((x , y+size)) 

    elif angle == 180: # if the angle is 180, move left
        coordinates.append((x-size , y)) 
    
    elif angle == 270: # if the angle is 270, move down
        coordinates.append((x , y-size)) 

def peanoCurve(order ,theta = 90, size = 1 , orient = 1): # function to draw the peano curve
   
    if order == 0: # if the order is 0, base case
        return 

    else:
        if orient == 1: # if the orientation is 1, print original peano curve
            
            peanoCurve(order-1,theta,size) # call the function recursively
            forward(size,theta) # move forward
            
            peanoCurve(order-1,theta,size,-orient) # call the function recursively but invert it every even call
            forward(size,theta) # move forward
            
            peanoCurve(order-1,theta,size) # call the function recursively 

            theta = right(theta) # turn right
            forward(size,theta) # move forward
            theta = right(theta) # turn right
            
            peanoCurve(order-1,theta,size,-orient) # call the function recursively but invert it every even call
            forward(size,theta) # move forward
            
            peanoCurve(order-1,theta,size) # call the function recursively
            forward(size,theta) # move forward
            
            peanoCurve(order-1,theta,size,-orient) # call the function recursively but invert it every even call

            theta = left(theta) # turn left
            forward(size,theta) # move forward  
            theta = left(theta) # turn left

            peanoCurve(order-1,theta,size) # call the function recursively
            forward(size,theta) # move forward
            
            peanoCurve(order-1,theta,size,-orient) # call the function recursively but invert it every even call
            forward(size,theta) # move forward
            
            peanoCurve(order-1,theta,size) # call the function recursively
        
        elif orient == -1: # if the orientation is -1, print the inverse peano curve (flipped horizontally)

            peanoCurve(order-1,theta,size) # call the function recursively
            forward(size,theta) # move forward
            
            peanoCurve(order-1,theta,size,-orient) # call the function recursively but invert it every even call
            forward(size,theta) # move forward
            
            peanoCurve(order-1,theta,size) # call the function recursively

            theta = left(theta) # turn left
            forward(size,theta) # move forward
            theta = left(theta) # turn left
            
            peanoCurve(order-1,theta,size,-orient) # call the function recursively but invert it every even call
            forward(size,theta) # move forward
            
            peanoCurve(order-1,theta,size) # call the function recursively
            forward(size,theta) # move forward
            
            peanoCurve(order-1,theta,size,-orient) # call the function recursively but invert it every even call

            theta = right(theta) # turn right
            forward(size,theta) # move forward
            theta = right(theta) # turn right

            peanoCurve(order-1,theta,size) # call the function recursively
            forward(size,theta) # move forward
            
            peanoCurve(order-1,theta,size,-orient) # call the function recursively but invert it every even call
            forward(size,theta) # move forward
            
            peanoCurve(order-1,theta,size) # call the function recursively

if __name__ == "__main__":
    o = int(input("Enter order of curve: ")) # get order of curve
    peanoCurve(o) # create peano curve
    print(f"Coordinates of Peano curve of order {o} are:\n{coordinates}") # print coordinates