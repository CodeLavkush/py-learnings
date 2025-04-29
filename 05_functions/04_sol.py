import math

def circle(radius):
    PI = math.pi

    def area():
        return round(PI * (radius ** 2), 4)

    def circumference():
        return round(2 * (PI * radius), 4)

    return area, circumference


radius = float(input("Enter circle radius: "))

area, cirecumference = circle(radius)

print("Area of circle is", area())
print("Circumference of circle is", cirecumference())
