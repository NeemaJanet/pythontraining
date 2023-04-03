


l=float(input("Enter the length of your cuboid: "))
w=float(input("Enter the width of your cuboid: "))
h=float(input("Enter the height of your cuboid: "))
area=2(l*h + l*w + h*w)
volume=l*w*h
def area(l,w,h):
    area=2 * (l * w + l* h + w * h)
    return("The surface area is:", area)

area()

def volume(l,w,h):
    vol=l * w * h
    return("The volume is:", volume)


volume()

