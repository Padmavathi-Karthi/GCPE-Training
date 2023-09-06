""" Allow users to mix operations with 3 numbers or more
e.g. 2 + 4 - 3, 4 *5 + 1 / 3 """


x = float(input("Enter the first number: "))
op1 = input("Enter operation (+, -, /, *): ")
y = float(input("Enter the second number: " ))
op2 = input("Enter operation (+, -, /, *, =): ")

if op1 == "+":
    ans1 = (x + y)
elif op1 == "-":
    ans1 = (x - y)
elif op1 == "/":
    ans1 = (x / y)
elif op1 == "*":
    ans1 = (x * y)
else:
    print("Invalid operator")

if op2 == "=":
    print(ans1)
elif op2 == "+":
    z = float(input("Enter the third number: " ))
    ans2 = print(ans1 + z)
elif op2 == "-":
    z = float(input("Enter the third number: " ))
    ans2 = print(ans1 - z)
elif op2 == "/":
    z = float(input("Enter the third number: " ))
    ans2 = print(ans1 / z)
elif op2 == "*":
    z = float(input("Enter the third number: " ))
    ans2 = print(ans1 * z)
else:
    print("Invalid operator")



