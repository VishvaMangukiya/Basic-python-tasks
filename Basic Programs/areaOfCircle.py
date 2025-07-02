def area_of_circle(r):
    pi = 3.14
    area = pi * r * r
    return area

print("Area of Circle\n")

r = float(input("Enter radius of circle: "))
area = area_of_circle(r)
print(f"The area of the circle is: {area}")
