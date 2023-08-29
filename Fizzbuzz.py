
# number = input("Enter your favourite number: ")

"""if number % 5 == 0 and number % 3 == 0:
    print("Fizzbuzz")
elif number % 5 == 0:
        print("Fizz")
elif number % 3 == 0:
        print("Buzz")"""

# FizzBuzz Execise: Example 1
limit = 21
counter = 1

while counter <= limit:
    #counter = counter + 1  # it will be incremented initially
    if counter % 3 == 0 and counter % 5 == 0:
        print("Fizzbuzz")
    elif counter % 3 == 0:
        print("Fizz")
    elif counter % 5 == 0:
        print("Buzz")
    else:
        print(counter)
    counter = counter + 1  # it would be incremented after the first number

print("\n")

# FizzBuzz Execise: Example 2

def fizzbuzz(n):
    for i in range(1, n+1):
        if i  % 3 == 0 and i % 5 == 0:
            print("Fizzbuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
fizzbuzz(50)

    
      



