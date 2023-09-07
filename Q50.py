"""
Rotate 90 degrees towards the right
Create a hilbert curve at level n-1 rotated by -90 degrees (ie, 90 degrees in anticlockwise direction)
Move step size
Rotate 90 degrees towards the right
Create a level n-1 hilbert curve rotated by 90 degrees (ie, 90 degrees in clockwise direction)
Rotate 90 degrees towards the left.
Move step size
Create a level n-1 hilbert curve rotated by -90 degrees
Rotate 90 degrees towards the right
"""

angle = 0 # angle of object in degrees 0 = right, 90 = up, 180 = left, 270 = down
coordinates = [(1,1)] # list of coordinates of the object

def right(theta): # function to rotate right
    theta -= 90 # rotate 90 degrees to the right
    theta = theta%360 # keep angle between 0 and 360
    return theta # return new angle

def left(theta): # function to rotate left
    theta += 90 # rotate 90 degrees to the left
    theta = theta%360 # keep angle between 0 and 360
    return theta # return new angle

def forward(size,angle): # function to move forward
    global coordinates  # use global variable coordinates
    x = coordinates[-1][0] # get x coordinate of last point
    y = coordinates[-1][1] # get y coordinate of last point
    if angle == 0: # if angle is 0
        coordinates.append((x+size , y)) # move point front by size
    
    elif angle == 90: # if angle is 90
        coordinates.append((x , y+size)) # move point up by size

    elif angle == 180: # if angle is 180
        coordinates.append((x-size , y)) # move point back by size
    
    elif angle == 270: # if angle is 270
        coordinates.append((x , y-size)) # move point down by size

def hilbertCurve(order,theta = 0, size = 1): # function to create hilbert curve
    global angle # use global variable angle

    if order == 0: # if order is 0
        return # return

    else: # if order is not 0
        theta = right(angle) # rotate right
        angle = -theta%360 # update angle for recursion
        hilbertCurve(order-1,-theta%360 , size) # create hilbert curve at level n-1 rotated by -90 degrees (ie, 90 degrees in anticlockwise direction)
        forward(size, -theta%360) # move step size

        theta = left(theta) # rotate left
        angle = theta # update angle for recursion
        hilbertCurve(order-1,theta , size) # create a level n-1 hilbert curve rotated by 90 degrees (ie, 90 degrees in clockwise direction)
        forward(size,theta) # move step size

        angle = theta # update angle for recursion
        hilbertCurve(order-1,theta , size) # create a level n-1 hilbert curve rotated by 90 degrees (ie, 90 degrees in clockwise direction)
        theta = left(theta) # rotate left
        angle = theta # update angle for recursion
        forward(size, -theta%360) # move step size

        angle = -theta%360 # update angle for recursion
        hilbertCurve(order-1,-theta%360 , size) # create a level n-1 hilbert curve rotated by -90 degrees (ie, 90 degrees in anticlockwise direction)
        angle = right(theta) # rotate right
  
# main
if __name__ == "__main__":
    o = int(input("Enter order of curve: ")) # get order of curve
    hilbertCurve(o) # create hilbert curve
    print(f"Coordinates of Hilbert curve of order {o} are:\n{coordinates}") # print coordinates