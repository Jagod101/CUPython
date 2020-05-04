#Zach Jagoda
#Student ID: 2274813
#Student Email: jagod101@mail.chapman.edu
#CPSC230
#In-Class Functions

import math

#Area of a Circle
def circleArea(radius):
    area = math.pi * (radius**2)
    return area

#Circumference of a Circle
def circleCircumference(radius):
    circumference = 2 * math.pi * radius
    return circumference

#Volume of a Sphere
def sphereVolume(radius):
    volume = (4/3) * math.pi * (radius**3)
    return volume

#Volume of a Cylinder
def cylinderVolume(radius, height):
    volume = math.pi * (radius**2) * height
    return volume

#User Input
choice = int(input("Please select an input:\n[1] Area of a Circle \n[2]Circumference of a Circle \n[3] Volume of a Sphere \n[4]Volume of a Sphere \nUser Input: "))
if choice == 1:
    circleRadius = float(input("Radius of your Circle: "))
    print("The Area of your Circle is: ", circleArea(circleRadius))
elif choice == 2:
    circleRadius = float(input("Radius of your Circle: "))
    print("The Circumference of your Circle is: ", circleCircumference(circleRadius))
elif choice == 3:
    sphereRadius = float(input("Radius of your Sphere: "))
    print("The Volume of your Sphere is: ", sphereVolume(sphereRadius))
elif choice == 4:
    cylinderRadius = float(input("Radius of your Cylinder: "))
    cylinderHeight = float(input("Height of your Cylinder: "))
    print("The Volume of your Cylinder is: ", cylinderVolume(cylinderRadius, cylinderHeight))
else:
    print("That wasn't valid input")
