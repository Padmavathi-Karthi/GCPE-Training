
food = input("What's the best food?: ")

if food == "rice":
    print("Yes, rice is the best.")
elif food.lower() == "apple":    # lower(), it will convert the user's input to lower case
    print("Apples aren't my cup of rice.")
elif food == "chicken":
    print("Chickens are good in proteins!")
else:
    print("Never heard of it!")
    
new_food = input("What is your second best food?: ")
if new_food == "rice":
    print("Yes this food is best")
else:
    print("Not in the list!")

print("/n")

# Example 1:

answer = input("What are your favourite trainers? type 'j' for Jordan's, 'd' for Dunks or 'a' for Ant! ")
while answer != "j" and answer != "d" and answer != "a":
    answer = input("That is not a valid response, type 'j', 'd' or 'a'!: ")
if answer == "j":
    print("You favourite trainers are Jordan's")
elif answer == "d":
    print("You favourite trainers are Dunks")
elif answer == "a":
    print("You favourite trainers are Ant")


print("/n")

# Example 2:

limit = 5
counter = 1
food = input("What's the best food?: ")
while counter < limit:
    if food != "chicken" and food != "rice":
        print("This food is not in the list!")
    #elif food == "chicken" or food == "rice":
        #print("This food is in the list!")
    else:
        print("This food is in the list!")

    counter = counter + 1

