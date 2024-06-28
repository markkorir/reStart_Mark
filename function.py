def volume(l, w, h):
    volume=l*w*h
    return volume

length = int(input("Enter the length "))
width = int(input("Enter the width "))
height = int(input("Enter the hieght "))

print("The volume is ", volume(length, width, height))