a = int(input("size of the first side of the triangle: "))
b = int(input("size of the second side of the triangle: "))
c = int(input("size of the third side of the triangle: "))
if a + b > c and a + c > b and b + c > a:
    print("The triangle is valid.")
    if a == b == c:
        print("The triangle is equilateral.")
    elif a == b or a == c or b == c:
        print("The triangle is isosceles.")
    elif a!= b and a != c and b != c:
        print("The triangle is scalene.")
else:
    print("The triangle is not valid.")