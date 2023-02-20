#Radian
import math
def radian(degree):
    rad = degree * math.pi / 180
    return rad
degree = int(input("Input degree: "))
print ("Radian:",radian(degree))

#Trapezoid
def area_of_trapezoid(height, basefirst, basesecond):
    area = (basefirst + basesecond)/2 * height
    return area
# height = int(input("Height: "))
# basefirst = int(input("Base, first value: "))
# basesecond = int(input("Base, second value: "))
# print ("Area of Trapezoid:" , area_of_trapezoid(height,basefirst,basesecond))

#Polygon
import math
def area_of_polygon(number_of_side, size_of_side):
    area = (number_of_side * size_of_side ** 2)/(4*math.tan(math.pi/number_of_side))
    return area
number_of_side = int(input("Input number of sides: "))
size_of_side = int(input("Input the length of a side: "))
print("Area of Polygon:" , area_of_polygon(number_of_side, size_of_side))

#Parallelogram
def area_of_parallelogram(leght,height):
    area = leght * height
    return area
# leght = int(input("Length of base: "))
# height = int(input("Height of parallelogram: "))
# print ("Area of parallelogram:", area_of_parallelogram(leght,height))