a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = input("Enter operator (+, -, *, /): ")
if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "*":
    print(a * b)
elif c == "/":
    if b != 0:
        print(a / b)
    else:
        print("Error: Division by zero")
else:
    print("Invalid operator")
