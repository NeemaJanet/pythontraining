def volume(l,w,h):
    area=2*(l*w+w*h+h*l)
    volume=l*w*h
    return (volume)

def area(l,w,h):
    area=2*(l*w+w*h+h*l)
    return (area)


l=float(input("Enter the length of your cuboid: "))
w=float(input("Enter the width of your cuboid: "))
h=float(input("Enter the height of your cuboid: "))

print("The volume is",volume(l,w,h))
print("The area is",area(l,w,h))




