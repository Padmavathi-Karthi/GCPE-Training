""" Instructions :
Write a program that takes two input numbers, then adds them together and prints the result.

# Extra time
If you complete this task then please try adding the following features:
* Take two numbers and subtract the second from the first number.
* Take two numbers and multiply the two.
* Take two numbers and divide the first number by the second number.
* Take two numbers and perform a modulus operation.
* Allow users to choose which operation they want to perform on two numbers.
* Take 3 numbers and add them together.
* Allow users to mix operations with 3 numbers or more
e.g. 2 + 4 - 3, 4 *5 + 1 / 3 """

num1 = 5
num2 = 10

# 1. Add
sum = int(num1) + int(num2) 
print(sum)

# 2. Subtraction
difference = int(num2) - int(num1)
print(difference)

# 3. Multiplication
multiply = int(num1) * int(num2)
print(multiply)

# 4. Division
division = int(num1) / int(num2)
print(division)

# 5. Modulus
modulus = int(num1) % int(num2)
print(modulus)

print("\n")

# 6.  Calculator task




num3 = int(input("Enter first number: "))
num4 = int(input("Enter second number: "))
print("\n")
print("******* Calculator Task*******")

print("Please select an option: ")
print("1. To Add")
print("2. To Subtract")
print("3. To Multiply")
print("4. To Divide")
print("5. To Modulus")

print("********************************")
print("\n")
options = ["1", "2", "3", "4", "5"]
userchoice = input("Enter an option from the above lists: ")

add = num3 + num4
sub = num4 - num3
multi = num3 * num4
div = num3 / num4
modulo = num3 % num4



if userchoice == "1":
        print(add)
elif userchoice == "2":
        print(sub)
elif userchoice == "3":
        print(multi)
elif userchoice == "4":
        print(div)
elif userchoice == "5":
        print(modulo)
else:
        print("Invalid choice")

input("Press enter to exit the application")

print("\n")



