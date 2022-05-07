from ast import Num
import math

square = float(input('What is the length of a side of the square?'))
areaSquare = math.pow(square, 2)
print(f"The area of the square is: {areaSquare}")

rectangleL = float(input('What is the length of the rectangle?'))
rectangleW = float(input('What is the width of the rectangle?'))
areaRectangle = (rectangleL * rectangleW)
print(f"The area of the rectangle is: {areaRectangle}")

radius = float(input('What is the radius of the circle?'))
areaCircle = math.pi * math.pow(radius, 2)
print(f"The area of the circle is: {areaCircle}")

singleValue = float(input('List a single length value:'))
sSquare = singleValue ** 2
sCirle = math.pi * (singleValue ** 3)
sCube = singleValue ** 3
sSphere = (4 / 3) * math.pi * (singleValue ** 3)

print(f"Area of a square: {sSquare}")
print(f"Area of a circle: {sCirle}")
print(f"Volume of a cube: {sCube}")
print(f"Volume of a sphere: {sSphere}")

sideCm = float(input('What is the length of a side of the square in cm?'))
areaSquareCm = sideCm ** 2

print(f"The area of the square is: {areaSquareCm} cm^2")
print(f"The area of the square is: {areaSquareCm / 10000} m^2")

lengthRectCm = float(input('What is the length of rectangle in cm?'))
widthRectCm = float(input('What is the width of the rectangle in cm?'))
areaRectCm = lengthRectCm * widthRectCm
print(f"The area of the rectangle is: {areaRectCm} cm^2")
print(f"The area of the rectangle is: {areaRectCm / 10000} m^2")

radiusCircleCm = float(input('What is the radius of the circle in cm?'))
areaCircleCm = math.pi * (radiusCircleCm ** 2)
print(f"The area of the circle is: {areaCircleCm} cm^2")
print(f"The area of the circle is: {areaCircleCm / 10000} m^2")
