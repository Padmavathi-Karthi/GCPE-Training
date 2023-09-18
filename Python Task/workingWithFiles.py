# Method 1

with open('Variables/Python Task/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)  

    #print(contents.rstrip())   # rstip() method removes or stripes any whitespace character from the right side of a string.

    #print(contents.lstrip())   # lstip() method removes or stripes any whitespace character from the leftt side of a string.

# Method 2

filename = 'Variables/Python Task/pi_digits.txt'

with open(filename) as file_object:
        for line in file_object:
            print(line)
            #print(line.rstrip())

# Method 3

filename = 'Variables/Python Task/pi_digits.txt'

with open(filename) as file_object:
        lines = file_object.readlines()
        
for line in lines:
            print(line)
            #print(line.rstrip())

# Method 4

pi_string = ''

for line in lines:
    #pi_string += line.rstrip()
    pi_string += line.strip()


print(pi_string)
print(len(pi_string))

# Method 5

filename = 'Variables/Python Task/pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:50]+ "...")
print(len(pi_string))

# Method 6

filename = 'Variables/Python Task/pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''

for line in lines:
    pi_string += line.rstrip()

birthday = input("Enter your birthday, in the form mmddyy: ")

if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")



